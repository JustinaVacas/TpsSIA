import numpy as np


# N es la dim de cada entrada --> 2 = {-1,1}
# p cantidad de entradas del conjunto de entrenamiento --> son 4 = {{−1, 1}, {1, −1}, {−1, −1}, {1, 1}}
# x conjunto de entrenamiento con dim N+1 = {-1,1}
# y salida deseada
# n taza de aprendizaje
# w es el vector de pesos ’sin´apticos’ que incluye el umbral
# signo funcion de activacion

def calculate_error(x, y, w, p):
    error = 0
    for i in range(p):
        o = y[i] - np.sign(np.dot(x[i], w))
        error += abs(o - y[i])
    return error


def simple_perceptron(p, n, x, y):
    i = 0
    limit = 1000
    w = np.zeros(len(x[0]))
    print("w = ", w)
    error = 1
    error_min = p * 2
    w_min = 0
    while error > 0 and i < limit:
        print("i = ", i)
        i_x = np.random.randint(0, p)  # 0 1 2 3
        print("i_x = ", i_x)
        h = np.dot(x[i_x], w)  # calculate excitation
        print("h = ", h)
        output = np.sign(h)  # calculate activation
        print("output = ", output)

        # delta_w = n * (y[i_x] - output) * x[i_x]
        # w[i_x] += delta_w

        for j in range(0, len(w)):
            delta_w = n * (y[i_x] - output) * x[i_x][j]
            w[j] += delta_w

        error = calculate_error(x, y, w, p)
        if error < error_min:
            error_min = error
            w_min = w
        i += 1

    print("i = ", i)
    print("y = ", y)
    print("w_min = ", w_min)


x = [[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]]
y = [-1, -1, -1, 1]
p = len(x)
n = 0.1     # taza aprendizaje
simple_perceptron(p, n, x, y)
