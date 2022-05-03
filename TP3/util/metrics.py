import numpy as np
from matplotlib import pyplot as plt


def evaluate(p, x, y, w, p_type, beta):
    return 0, 0


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
