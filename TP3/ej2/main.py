from numpy import array
from TP3.util.simple_perceptron import simple_perceptron, plot


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

min_out = min(outputs)
max_out = max(outputs)

p = len(inputs)
n = 0.1  # taza aprendizaje
limit = 1000
beta = 0.5

plot(inputs, outputs, simple_perceptron(p, n, inputs, outputs, limit, 'linear', beta), limit)

plot(inputs, outputs, simple_perceptron(p, n, inputs, outputs, limit, 'not_linear', beta), limit)


