import time

import numpy as np
from matplotlib import pyplot as plt


def sign(h):
    return 1 if h >= 0 else -1


def calculate_error(x, y, w, p):
    error = 0
    for i in range(p):
        h = np.dot(x[i], w)
        output = sign(h)
        error += abs(output - y[i])
    return error


def step_train(p, n, x, y, limit):
    i = 0
    w = np.zeros(len(x[0]))
    error = 1
    error_min = p * 2
    w_min = w
    all_weights = []

    start_time = time.process_time()
    while error > 0 and i < limit:
        i_x = np.random.randint(0, p)  # 0 1 2 3
        h = np.dot(x[i_x], w)  # calculate excitation
        output = sign(h)

        for index in range(3):
            delta_w = n * (y[i_x] - output) * x[i_x][index]
            w[index] += delta_w

        error = calculate_error(x, y, w, p)
        if error < error_min:
            error_min = error
            w_min = w
        i += 1
        all_weights.append(np.copy(w))

    end_time = time.process_time()
    print('------ Training... --------')
    print("Iterations = ", i)
    print("Time: " + str(end_time - start_time) + " s")
    print("Error_min = ", error_min)
    print("Weights: ", w_min)
    plot(x, y, all_weights, i)
    print('\n')

    return w


def plot(inputs, outputs, weights, limit):
    fig, ax = plt.subplots()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    for i in range(len(inputs)):
        if outputs[i] == -1:
            color = "black"
        else:
            color = "red"
        ax.scatter(inputs[i][1], inputs[i][2], color=color)
    plt.axhline(y=0, xmin=-1, xmax=1, color="grey")
    plt.axvline(x=0, ymin=-1, ymax=1, color="grey")

    # en la 1000 ya aprendio
    a = -(weights[limit - 1][1] / weights[limit - 1][2])  # -(w1/w2)
    b = -(weights[limit - 1][0] / weights[limit - 1][2])  # w0/w2
    y = lambda x: a * x + b  # clasifica entre los -1 y 1
    ax.plot([-2, 2], [y(-2), y(2)], color="blue")

    plt.title("Perceptron simple")
    plt.show()
