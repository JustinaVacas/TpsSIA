import math
import numpy as np


def function(individual, point):
    sum1 = 0
    for j in range(2):
        sum2 = 0
        for k in range(3):
            sum2 += individual[3 * (j + 1) + k] * point[k]
        sum2 -= individual[9 + j]
        sum1 += individual[j + 1] * g(sum2)
    sum1 -= individual[0]

    return g(sum1)


def g(x):
    return (np.exp(x)) / (1 + np.exp(x))


def error(individual, output, points):
    aux = 0
    for i in range(3):
        aux += np.float_power((output[i] - function(individual, points[i])), 2)

    return 3-aux
