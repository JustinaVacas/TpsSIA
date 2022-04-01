import math

# individual [W0 W1 W2 w11 w12 w13 w21 w22 w23 w01 w02 ]
#             0  1  2   3   4   5   6   7   8  9   10
# rulo[ A B C ]
#        0 1 2

# range(3,6)  -->  3 4 5
# range(6,9)  -->  6 7 8


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
    return aux


# individual = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]
# rulo1 = [4.4793, -4.0765, -4.0765]
# rulo2 = [-4.1793, -4.9218, 1.7664]
# rulo3 = [-3.9429, -0.7689, 4.8830]
# print("rulo1 = ", function(individual, rulo1))
# print("rulo2 = ", function(individual, rulo2))
# print("rulo2 = ", function(individual, rulo3))
#
# sol = [0, 1, 1]
# rulos = [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]]
# print("error = ", error(individual, sol, rulos))
