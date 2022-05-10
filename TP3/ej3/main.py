import json

import numpy as np
from TP3.util.multiple_perceptron import MultilayerPerceptron

with open("./ej3/config.json") as f:
    config = json.load(f)

ex = config["exercise"]
batch = config["batch"]
momentum = config["momentum"]
learning_rate = config["learning_rate"]
beta = config["beta"]
epochs_amount = config["epochs_amount"]
hidden_layers = config["hidden_layers"]

adaptive_eta = config["adaptive_eta"]["use"]
adaptive_eta_increase = config["adaptive_eta"]["increase_by"]
adaptive_eta_decrease = config["adaptive_eta"]["decrease_by"]
adaptive_eta_max_iterations = config["adaptive_eta"]["max_iterations"]
adaptive_eta_params = [adaptive_eta, adaptive_eta_increase, adaptive_eta_decrease, adaptive_eta_max_iterations]

with open('./ej3/entrenamiento.txt') as f1:
    lines = f1.readlines()
    values = []
    row = 0
    aux = str
    for entry in lines:
        if row == 0:
            aux = entry
            row += 1
        if row == 7:
            float_vals = [*list(map(lambda v: int(v), aux.split()))]
            values.append(float_vals)
            row = 0
        else:
            aux += entry
            row += 1

    inputs = np.array(values)
    f1.close()

if ex == 1:
    # Parte 1
    print("------ Ejercicio 1 ------")
    inputs = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    outputs = [1, 1, -1, -1]

    mp1 = MultilayerPerceptron(inputs, outputs, learning_rate, hidden_layers, adaptive_eta_params, beta, batch, momentum)
    mp1.train(epochs_amount)

    results = np.array(mp1.get_output(inputs), dtype=float)

    print('Resultados:')
    print("Esperado\t   \t\tReal")
    error = 0
    for i in range(results.size):
        print('  ', outputs[i], "\t-->\t", f'{results[i][0]}')
        error += abs(outputs[i]-results[i][0])
    print('Total Error: ', f'{error / len(results)}')
    print('\n')

# Parte 2
elif ex == 2:
    print("------ Ejercicio 2 ------")

    training_set = inputs[:5]
    test_set = inputs[5:]
    expected_outputs = [1, -1] * 5

    mp2 = MultilayerPerceptron(training_set, expected_outputs, learning_rate, hidden_layers, adaptive_eta_params, beta, batch, momentum)
    mp2.train(epochs_amount)

    results = np.array(mp2.get_output(test_set), dtype=float)
    print('Resultados:')
    print("Esperado\t   \t\tReales")
    error = 0
    for i in range(results.size):
        print('  ', expected_outputs[i], "\t\t-->\t\t", np.round(results[i])[0])
        error += abs(expected_outputs[i]-np.round(results[i][0]))
    print('Total Error: ', f'{error/len(results)}')

# Parte 3
elif ex == 3:
    print("------ Ejercicio 3 ------")
    training_set = inputs
    outputs = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    # for num in range(10):
    #     expected_output = [-1] * 10
    #     expected_output[num] = 1
    #     outputs.append(expected_output)

    mp3 = MultilayerPerceptron(training_set, outputs, learning_rate, hidden_layers, adaptive_eta_params, beta, batch, momentum)
    mp3.train(epochs_amount)

    test_inputs = []
    for k in range(10):
        for i, picture in enumerate(inputs):
            picture_copy = np.copy(picture)
            for j in range(len(picture)):
                rnd = np.random.uniform()
                if rnd < 0.02:
                    picture_copy[j] = 1 - picture_copy[j]

            test_inputs.append(picture_copy)

    results = np.array(mp3.get_output(test_inputs), dtype=float)
    print('Resultados:')
    print("Esperado", "\t-->\t", "\t\t\tError")
    error = 0
    for i in range(10):
        print(outputs[i], "\t\t-->\t\t", outputs[i]-results[i][0])
        error += abs(outputs[i]-results[i][0])
    print("Total error: ", error)
