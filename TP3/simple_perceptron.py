import numpy as np
import matplotlib.pyplot as plt


# N es la dim de cada entrada --> 2 = {-1,1}
# p cantidad de entradas del conjunto de entrenamiento --> son 4 = {{−1, 1}, {1, −1}, {−1, −1}, {1, 1}}
# x conjunto de entrenamiento con dim N+1 = {-1,1}
# y salida deseada
# n taza de aprendizaje
# w es el vector de pesos ’sin´apticos’ que incluye el umbral
# signo funcion de activacion

def calculate_error(x, y, w, p):
    error = 0
    for i in range(p):
        o = y[i] - np.sign(np.dot(x[i], w))
        error += abs(o - y[i])
    return error

def simple_perceptron(p, n, x, y, limit):
    i = 0
    w = np.zeros(len(x[0]))
    error = 1
    error_min = p * 2
    w_min = 0
    weights = []
    while error > 0 and i < limit:
        i_x = np.random.randint(0, p)  # 0 1 2 3
        h = np.dot(x[i_x], w)  # calculate excitation
        output = np.sign(h)  # calculate activation

        # delta_w = n * (y[i_x] - output) * x[i_x]
        # w[i_x] += delta_w

        for j in range(0, len(w)):
            delta_w = n * (y[i_x] - output) * x[i_x][j]
            w[j] += delta_w

        error = calculate_error(x, y, w, p)
        if error < error_min:
            error_min = error
            w_min = w
        i += 1
        weights.append(np.copy(w))

    print("i = ", i)
    print("y = ", y)
    print("w_min = ", w_min)
    print("weights = ", weights)

    plot(x, y, weights, limit)


def plot(input, output, weights, limit):
    fig, ax = plt.subplots()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    for i in range(len(input)):
        if output[i] == -1:
            color = "black"
        else:
            color = "red"
        ax.scatter(input[i][1], input[i][2], color=color)
    plt.axhline(y=0, xmin=-1, xmax=1, color="grey")
    plt.axvline(x=0, ymin=-1, ymax=1, color="grey")

    # en la 1000 ya aprendio
    a = -(weights[limit-1][1] / weights[limit-1][2])    # -(w1/w2)
    b = -(weights[limit-1][0] / weights[limit-1][2])    # w0/w2
    y = lambda x: a * x + b                             # clasifica entre los -1 y 1
    ax.plot([-2, 2], [y(-2), y(2)], color="blue")

    plt.title("Perceptron simple")
    plt.show()


