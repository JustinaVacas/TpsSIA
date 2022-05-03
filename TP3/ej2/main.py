from numpy import array

from TP3.util.linear_perceptron import linear_train
from TP3.util.metrics import evaluate, plot
from TP3.util.not_linear_perceptron import not_linear_train

with open('entradas.txt') as f1:
    lines = f1.readlines()
    values = []

    for entry in lines:
        float_vals = [*list(map(lambda v: float(v), entry.split()))]
        values.append(float_vals)

    inputs = array(values)
    f1.close()

with open('salidas.txt') as f2:
    lines = f2.readlines()
    values = []

    for entry in lines:
        float_vals = list(map(lambda v: float(v), entry.split()))[0]
        values.append(float_vals)

    outputs = array(values)
    f2.close()

p = len(inputs)
n = 0.01  # taza aprendizaje
limit = 1000
beta = 0.1

# ------------ Lineal --------------- #

# Training
w_linear, linear_error = linear_train(p, n, inputs, outputs, limit)
# plot(inputs, outputs, w_linear, limit)

# ------------ No Lineal --------------- #

# Training
train_inputs = inputs[:150]
normalized_outputs = list(map(lambda x: x * (10 ** -2), outputs[:150]))     # escalamos los valores deseados entre 0 y 1
train_p = len(train_inputs)

w_not_linear, not_linear_error = not_linear_train(train_p, n, train_inputs, normalized_outputs, limit, beta)
# plot(train_inputs, outputs, w_not_linear, limit)

# Test
test_inputs = inputs[150:]
test_outputs = outputs[150:]
test_p = len(test_inputs)
hits, error = evaluate(test_p, test_inputs, test_outputs, w_not_linear, 'not_linear', beta)

