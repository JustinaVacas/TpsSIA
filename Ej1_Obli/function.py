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


def error(x):
    points = [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]]
    output = [0, 1, 1]
    aux = 0
    for i in range(3):
        aux += (output[i] - function(x, points[i])) ** 2
    return aux
