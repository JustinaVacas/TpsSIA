
from TP3.simple_perceptron import simple_perceptron

# and
input = [[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]]
output = [-1, -1, -1, 1]
# or
# input = [[1, -1, 1], [1, 1, -1], [1, -1, -1], [1, 1, 1]]
# output = [1, 1, -1, -1]
p = len(input)
n = 0.1  # taza aprendizaje
limit = 1000
simple_perceptron(p, n, input, output, limit)

# conclusiones
# el or no tiene solucion, porque no se pueden separar los rojos de los negros