import time
from math import tanh

import numpy as np


def g(h, beta):
    return tanh(beta * h)


def g_prime(h, beta):
    return beta * (1 - g(h, beta)**2)


def calculate_error(x, y, w, p, beta):
    error = 0
    for i in range(p):
        h = np.dot(w, x[i])
        output = g(h, beta)
        output = output * (10 ** 2)  # usamos la inversa de la función de normalización
        error += (y[i] - output)**2
    return 0.5 * error


def not_linear_train(p, n, x, y, limit, beta):
    i = 0
    w = np.zeros(len(x[0]))
    error = 1
    error_min = -1
    w_min = np.zeros(len(x[0]))

    start_time = time.process_time()
    while error > 0 and i < limit:
        i_x = np.random.randint(0, p)  # 0 1 2 3
        h = np.dot(x[i_x], w)  # calculate excitation

        output = g(h, beta)

        delta_w = n * (y[i_x] - output) * g_prime(h, beta) * x[i_x]
        w = w + delta_w

        error = calculate_error(x, y, w, p, beta)
        if error < error_min or error_min == -1:
            error_min = error
            w_min = w
        i += 1

    end_time = time.process_time()
    print('------ Training... --------')
    print("Iterations = ", i)
    print("Time: " + str(end_time - start_time) + " s")
    print("Error_min = " + str(error_min))
    print('\n')

    return w_min, error_min
