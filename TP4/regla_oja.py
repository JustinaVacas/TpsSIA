import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def regla_oja():
    n = 0.01
    total_neurons = 28
    max_epochs = 500 * total_neurons
    # TODO chequear que esten bien los parametros

    np.set_printoptions(suppress=True, linewidth=np.inf)  # para que no me ponga exponenciales

    dataset = pd.read_csv('europe.csv')

    x = dataset.iloc[:, 1:].values  # features
    y = dataset.iloc[:, 0].values  # countries names

    data = StandardScaler().fit_transform(x)

    # seteo los pesos iniciales
    weight = np.random.uniform(-1, 1, len(data[0]))
    w = [weight]
    iterations = 0
    while iterations < max_epochs:
        for j in range(total_neurons):
            aux = 0
            for i in range(len(data[j])):
                aux += data[j][i] * weight[i]
            s = aux
            weight = weight + n * s * (data[j] - s * weight)
            w.append(weight)
        iterations += 1
    print("Autovector", w[-1])  # devulve el ultimo array
    primer_componente = np.matmul(data, w[-1])  # producto vectorial de data y el autovector
    print("Primer componente", primer_componente)

if __name__ == "__main__":
    regla_oja()
