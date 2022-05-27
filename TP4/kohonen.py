import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def set_weights(data, k):
    weights = []
    for i in range(k * k):
        wi = data[np.random.randint(len(data))]
        weights.append(wi)
    return np.array(weights)  # [[1,...,7]...[1,...,7]]


def get_winner(x_p, weights):
    min = 0
    index = 0
    for n in range(len(weights)):
        aux = np.linalg.norm(x_p - weights[n])
        if n == 0:
            min = aux
        else:
            if aux < min:
                min = aux
                index = n
    return index


def update_neighbours(weights, radio, w_k, n, x_p):
    neu_k = weights[w_k]
    n_k = []
    for i in range(len(weights)):
        if i != w_k and np.linalg.norm(weights[i] - neu_k) < radio:
            n_k.append(i)
    np.array(n_k)
    print("n_k", n_k)

    for j in range(len(weights)):
        if j in n_k:
            weights[j] = weights[j] + n * (x_p - weights[j])
    print("weights", weights)


def kohonen():
    total_neurons = 28
    k = 5
    n = 0.01
    max_epochs = 500 * total_neurons
    radio = 2**(1/2)
    # TODO chequear que esten bien los parametros

    np.set_printoptions(suppress=True, linewidth=np.inf)  # para que no me ponga exponenciales

    dataset = pd.read_csv('europe.csv')

    x = dataset.iloc[:, 1:].values     # features
    y = dataset.iloc[:, 0].values      # countries names

    data = StandardScaler().fit_transform(x)
    print("Variables estandarizadas\n", data)

    # seteamos los pesos
    weights = set_weights(data, k)
    print("weights\n", weights)

    iteration = 1
    while iteration < max_epochs:

        # selecciono un registro de la entrada
        x_p = data[np.random.randint(len(data))]
        print("x_p", x_p)

        # encontrar neurona ganadora
        w_k = get_winner(x_p, weights)
        print("w_k", w_k)

        # actualizar los pesos de las neuronas vecinas
        update_neighbours(weights, radio, w_k, n, x_p)

        iteration += 1
        n = 1 / iteration
        if radio > 0:
            radio -= 1
            if radio < 0:
                radio = 1


if __name__ == "__main__":
    kohonen()
