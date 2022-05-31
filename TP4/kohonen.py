import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import Tuple
import matplotlib.pyplot as plt
import seaborn as sns


class Neuron:
    def __init__(self, weights, count, position):
        self.weights = weights
        self.count = count
        self.position = position
        self.elements = np.array([])

    def add(self, elem):
        self.elements = np.append(self.elements, elem)


def get_neighbors(i, j):
    return [(i, j + 1), (i + 1, j), (i + 1, j + 1), (i, j - 1), (i - 1, j), (i - 1, j - 1), (i - 1, j + 1),
            (i + 1, j - 1)]


def plt_matrixU(k, grid):
    u_values = np.zeros((k, k), float)
    plt.figure(figsize=(20, 10))

    for i in range(k):
        for j in range(k):
            aux = np.linalg.norm(grid[i, j].weights)
            w = grid[i, j].weights / aux
            neighbors = get_neighbors(i, j)
            distances = []
            for n in neighbors:
                x, y = n[0], n[1]
                if x >= 0 and y >= 0 and x < k and y < k:
                    aux = np.linalg.norm(np.array(grid[x, y].weights))
                    neighbor_neuron_w = grid[x, y].weights / aux
                    dist = np.linalg.norm(w - neighbor_neuron_w)
                    distances.append(dist)

            u_values[i][j] = np.mean(distances)

    sns.heatmap(u_values, annot=True, cmap='YlGnBu')

    plt.savefig('matrixU.png')
    plt.show()


def plt_map(k, grid, countries,data):
    values = np.zeros((k, k), int)
    index = 0
    for elem in data:
        position_min = (None, None)
        min_dist = 999
        for i in grid:
            for j in i:
                w = j.weights
                dist = np.linalg.norm(elem - w)
                if dist < min_dist:
                    position_min = j.position
                    min_dist = dist
        grid[position_min[0], position_min[1]].add(countries[index])
        grid[position_min[0], position_min[1]].count += 1
        values[position_min[0], position_min[1]] += 1
        index += 1

    fig, ax = plt.subplots(figsize=(20, 10))
    x = 0
    for col in grid:
        for y in range(len(col)):
            label = ''
            for e in grid[x][y].elements:
                label = label + str(e) + '\n'
            ax.text(y + 0.1, x + 0.75, label, color = "r")
        x += 1

    sns.heatmap(values, annot=True, ax=ax, cmap="YlGnBu")
    plt.savefig('matrix.png')
    plt.show(block=False)


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


def create_grid(weights, k):
  grid = np.empty((k, k), Neuron)
  index = 0
  for i in range(k):
      for j in range(k):
          grid[i][j] = Neuron(weights[index], 0, (i, j))
          index += 1
  return grid


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

    grid = create_grid(weights, k)

    plt_map(k, grid, y, data)
    plt_matrixU(k, grid)


if __name__ == "__main__":
    kohonen()
