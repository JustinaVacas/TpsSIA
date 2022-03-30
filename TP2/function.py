import math

#individual [W0 W1 W2 w11 w12 w13 w21 w22 w23 w01 w02 ]
#             0  1  2   3   4   5   6   7   8  9   10
#rulo[ A B C ]
#        0 1 2

# range(3,6)  -->  3 4 5
# range(6,9)  -->  6 7 8


def function(individual, rulo):
    aux = aux2 = aux3 = aux5 = aux4 = 0
    for i in range(1, 3):
        aux = 0
        aux2 = 0
        aux3 = 0
        aux6 = 0
        for j in range(3*i, 3+3*i):
            aux += individual[j] * rulo[j-3*i] - individual[8+i]     # w10 w20
        aux2 = g(aux)
        aux3 += individual[i] * aux2    # SUM( W * g(...) )
        print("aux3", aux3)
        aux4 += aux3 - individual[0]

        # aux6 = aux3 - individual[0]
        # print("aux6", aux6)

    print("aux4", aux4)
    aux5 = g(aux4)
    return aux5


def g(x):
    return (math.exp(x))/(1+math.exp(x))


# sol = [0,1,2]
def error(individual, sol, rulos):
    aux = 0
    for i in range(3):
        aux += math.pow(sol[i] - function(individual, rulos[i]), 2)
    return aux

individual = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]
rulo = [4.4793, -4.0765, -4.0765]
print(function(individual, rulo))

# def error(individual):