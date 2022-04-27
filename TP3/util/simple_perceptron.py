import time
from math import tanh

import numpy as np
import matplotlib.pyplot as plt


# N es la dim de cada entrada --> 2 = {-1,1}
# p cantidad de entradas del conjunto de entrenamiento --> son 4 = {{−1, 1}, {1, −1}, {−1, −1}, {1, 1}}
# x conjunto de entrenamiento con dim N+1 = {-1,1}
# y salida deseada
# n taza de aprendizaje
# w es el vector de pesos ’sin´apticos’ que incluye el umbral
# signo funcion de activacion


def calculate_error(y, output):
    return 0.5 * sum((y-output)**2)


def g(h, beta):
    return tanh(beta*h)


def g_prime(h, beta):
    return beta * (1 - g(h, beta) ** 2)


def simple_perceptron(p, n, x, y, limit, p_type, beta):
    i = 0
    w = np.zeros(len(x[0]))
    error = 1
    error_min = p * 2
    w_min = np.zeros(len(x[0]))
    weights = []
    start_time = time.process_time()
    while error > 0 and i < limit:
        i_x = np.random.randint(0, p)  # 0 1 2 3
        h = np.dot(x[i_x], w)  # calculate excitation

        # calculate activation
        if p_type == 'linear':
            output = h
        if p_type == 'not_linear':
            output = g(h, beta)
        else:
            output = np.sign(h)

        for j in range(0, len(w)):
            delta_w = n * (y[i_x] - output) * x[i_x][j]
            w[j] += delta_w

        error = calculate_error(y, output)
        if error < error_min:
            error_min = error
            w_min = w
        i += 1
        weights.append(np.copy(w))

    end_time = time.process_time()
    print("Perceptron " + p_type)
    print("Iterations = ", i)
    print("W_min = ", w_min)
    print("Weights ==> ", weights)
    print("Time: " + str(end_time-start_time) + " s")
    print('\n')

    return weights


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
