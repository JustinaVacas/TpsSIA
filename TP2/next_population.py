from random import random
from function import error
from population_0 import generate_initial_population


def apply_fitness(old_population):
    for X in old_population:
        X.fitness = error(X)


def select(population):
    return population[1], population[2]

def cross(x1, x2):
    return x2, x1


def create_next_population(population):
    i = 0
    while i < P:
    x1, x2 = select(population)
    n1, n2 = cross(x1, x2)
'''


def algorithm():
    population = generate_initial_population()
    apply_fitness(population)
    # new_population = create_next_population(population)

