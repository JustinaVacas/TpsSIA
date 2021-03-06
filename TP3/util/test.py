import numpy as np
from TP3.util.not_linear_perceptron import g, normalize_inverse
import matplotlib.pyplot as plt


def calculate_error(x, y, w, p, beta, t_max, t_min):
    print('------ Testing... --------')
    error = 0
    hits = 0
    error_range = 10
    for i in range(p):
        h = np.dot(w, x[i])
        output = normalize_inverse(g(h, beta), t_max, t_min)
        test = abs(y[i] - output)
        if test < error_range:
            hits += 1
        error += (y[i] - output) ** 2
    print("Test error = ", error)
    print("Hits = ", hits)
    return (1 / p) * error, hits
