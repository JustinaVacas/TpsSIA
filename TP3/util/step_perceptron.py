import time

import numpy as np


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
    error_min = -1
    w_min = w

    start_time = time.process_time()
    while error > 0 and i < limit:
        i_x = np.random.randint(0, p)  # 0 1 2 3
        h = np.dot(x[i_x], w)  # calculate excitation
        output = sign(h)

        delta_w = n * (y[i_x] - output) * x[i_x]
        w += delta_w

        error = calculate_error(x, y, w, p)
        if error < error_min or error_min == -1:
            error_min = error
            w_min = w
        i += 1

    end_time = time.process_time()
    print('------ Training... --------')
    print("Iterations = ", i)
    print("Time: " + str(end_time - start_time) + " s")
    print('\n')

    return w_min, error_min
