from TP3.util.simple_perceptron import simple_perceptron, plot

# and
and_inputs = [[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]]
and_outputs = [-1, -1, -1, 1]
# or
or_inputs = [[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]]
or_outputs = [1, 1, -1, -1]

p = len(and_inputs)
n = 0.1  # taza aprendizaje
limit = 1000
p_type = 'escalon'

plot(and_inputs, and_outputs, simple_perceptron(p, n, and_inputs, and_outputs, limit, p_type, 0), limit)

plot(or_inputs, or_outputs, simple_perceptron(p, n, or_inputs, or_outputs, limit, p_type, 0), limit)

# Conclusiones
# el or no tiene solucion, porque no se pueden separar los rojos de los negros
