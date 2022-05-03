import time

import numpy as np


def calculate_error(x, y, w, p):
    error = 0
    for i in range(p):
        output = np.dot(x[i], w)
        error += (y[i] - output) ** 2
    return 0.5 * error


def linear_train(p, n, x, y, limit):
    i = 0
    w = np.zeros(len(x[0]))
    error = 1
    error_min = -1
    w_min = np.zeros(len(x[0]))

    start_time = time.process_time()
    while error > 0 and i < limit:
        i_x = np.random.randint(0, p)  # 0 1 2 3
        output = np.dot(x[i_x], w)  # calculate excitation

        delta_w = n * (y[i_x] - output) * x[i_x]
        w = w + delta_w

        error = calculate_error(x, y, w, p)
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
