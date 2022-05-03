from TP3.util.step_perceptron import step_train

# and
and_inputs = [[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]]
and_outputs = [-1, -1, -1, 1]
# or
or_inputs = [[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]]
or_outputs = [1, 1, -1, -1]

n = 0.1  # taza aprendizaje
limit = 1000

and_weights = step_train(len(and_inputs), n, and_inputs, and_outputs, limit)

or_weights = step_train(len(or_inputs), n, or_inputs, or_outputs, limit)

# TODO: podriamos comparar los errores minimos y pesos en varios entrenamientos
# Conclusiones
# el or no tiene solucion, porque no se pueden separar los rojos de los negros
