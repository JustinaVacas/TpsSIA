import math


def g(x):
    return (math.exp(x)) / (1 + math.exp(x))


def function(x, point):
    sum1 = 0
    for j in range(2):
        sum2 = 0
        for k in range(3):
            sum2 += x[3 * (j + 1) + k] * point[k]
        sum2 -= x[9 + j]
        sum1 += x[j + 1] * g(sum2)
    sum1 -= x[0]

    return g(sum1)


def g2(x):
    return (math.exp(x)) / (1 + math.exp(x)**2)


def f_gradient(x, point):
    sum1 = 0
    for j in range(2):
        sum2 = 0
        for k in range(3):
            sum2 += x[3 * (j + 1) + k] * point[k]
        sum2 -= x[9 + j]
        sum1 += x[j + 1] * g2(sum2)
    sum1 -= x[0]

    return g2(sum1)


def error(x, output, points):
    aux = 0
    gradient = 0
    for i in range(3):
        aux += (output[i] - function(x, points[i])) ** 2
        gradient += (output[i] - f_gradient(x, points[i])) ** 2

    return aux, gradient
