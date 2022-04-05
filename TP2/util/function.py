import math


def function(individual, point):
    aux4 = 0
    for i in range(1, 3):
        aux = 0
        aux3 = 0
        for j in range(3 * i, 3 + 3 * i):
            aux += individual[j] * point[j - 3 * i] - individual[8 + i]  # w10 w20
        aux2 = g(aux)
        aux3 += individual[i] * aux2  # SUM( W * g(...) )
        aux4 += aux3 - individual[0]

    aux5 = g(aux4)
    return aux5


def g(x):
    return (math.exp(x)) / (1 + math.exp(x))



def error(individual, output, points):
    aux = 0
    for i in range(3):
        aux += math.pow(output[i] - function(individual, points[i]), 2)
    return 3 - aux
