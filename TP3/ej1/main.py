from TP3.util.metrics import plot
from TP3.util.step_perceptron import step_train

# and
and_inputs = [[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]]
and_outputs = [-1, -1, -1, 1]
# or
or_inputs = [[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]]
or_outputs = [1, 1, -1, -1]

p = len(and_inputs)
n = 0.1  # taza aprendizaje
limit = 1000

and_weights, and_error_min = step_train(p, n, and_inputs, and_outputs, limit)
plot(and_inputs, and_outputs, and_weights, limit)

or_weights, or_error_min = step_train(p, n, or_inputs, or_outputs, limit)
plot(or_inputs, or_outputs, or_weights, limit)

# TODO: podriamos comparar los errores minimos y pesos en varios entrenamientos
# Conclusiones
# el or no tiene solucion, porque no se pueden separar los rojos de los negros
