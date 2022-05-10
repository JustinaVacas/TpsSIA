import time
from math import tanh

import numpy as np
import matplotlib.pyplot as plt


def g(h, beta):
    return tanh(beta * h)


def g_prime(h, beta):
    return beta * (1 - g(h, beta) ** 2)


def normalize_inverse(x, t_max, t_min):
    return (((x + 1) / 2) * (t_max - t_min)) + t_min


def calculate_error(x, y, w, p, beta, t_max, t_min):
    error = 0
    error2 = 0
    aux = list(map(lambda o: normalize_inverse(o, t_max, t_min), y))
    for i in range(p):
        h = np.dot(w, x[i])
        output = g(h, beta)
        error2 += (y[i] - output) ** 2
        output = normalize_inverse(output, t_max, t_min)  # usamos la inversa de la función de normalización
        error += (aux[i] - output) ** 2
    return (1 / p) * error, (1 / p) * error2


def not_linear_train(p, n, x, y, limit, beta, t_max, t_min):
    i = 0
    w = np.zeros(len(x[0]))
    error = 1
    error2 = 1  # Error sin escalar
    error_min = -1
    error2_min = -1
    w_min = np.zeros(len(x[0]))

    start_time = time.process_time()
    while error > 0 and i < limit:
        i_x = np.random.randint(0, p)  # 0 1 2 3
        h = np.dot(x[i_x], w)  # calculate excitation

        output = g(h, beta)

        delta_w = n * (y[i_x] - output) * g_prime(h, beta) * x[i_x]
        w = w + delta_w

        error, error2 = calculate_error(x, y, w, p, beta, t_max, t_min)
        if error < error_min or error_min == -1:
            error_min = error
            w_min = w
        if error2 < error2_min or error2_min == -1:
            error2_min = error2
        i += 1

    end_time = time.process_time()
    print('------ Not Linear Training... --------')
    print("Iterations = ", i)
    print("Time: " + str(end_time - start_time) + " s")
    print("Error_min = " + str(error_min))
    print("Error_min (without scale) = " + str(error2_min))
    print('\n')

    return w_min, error_min, error2_min
