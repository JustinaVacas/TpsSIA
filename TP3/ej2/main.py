import numpy as np

from TP3.util.linear_perceptron import linear_train
from TP3.util.not_linear_perceptron import not_linear_train
from TP3.util.test import calculate_error

with open('entradas.txt') as f1:
    lines = f1.readlines()
    values = []

    for entry in lines:
        float_vals = [*list(map(lambda v: float(v), entry.split()))]
        values.append(float_vals)

    inputs = np.array(values)
    f1.close()

with open('salidas.txt') as f2:
    lines = f2.readlines()
    values = []

    for entry in lines:
        float_vals = list(map(lambda v: float(v), entry.split()))[0]
        values.append(float_vals)

    outputs = np.array(values)
    f2.close()

p = len(inputs)
n = 0.01  # taza aprendizaje
limit = 1000
beta = 0.7

# ------------ Lineal --------------- #

# Training
w_linear, linear_error = linear_train(p, n, inputs, outputs, limit)

# ------------ No Lineal --------------- #

# Training
train_inputs = inputs[:150]
train_outputs = outputs[:150]
train_p = len(train_inputs)

t_min = np.amin(train_outputs)
t_max = np.amax(train_outputs)
t_range = t_max - t_min
normalized_outputs = list(map(lambda x: 2 * ((x - t_min)/t_range) - 1, train_outputs))     # escalamos los valores deseados entre 0 y 1

w_not_linear, not_linear_error, not_linear_error2 = not_linear_train(train_p, n, train_inputs, normalized_outputs, limit, beta, t_max, t_min)

# Test
test_inputs = inputs[150:]
test_outputs = outputs[150:]
test_min = np.amin(test_outputs)
test_max = np.amax(test_outputs)
test_p = len(test_inputs)
error, hits = calculate_error(test_inputs, test_outputs, w_not_linear, test_p, beta, test_max, test_min)
print("Success: ", hits*100/50, "%")
