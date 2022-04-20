import numpy as np


class Individual:
    def __init__(self, genotype, fitness, error):
        self.genotype = genotype
        self.fitness = fitness
        self.error = error

    def __repr__(self):
        return "Genotype: " + str(self.genotype) + '\n' + "Fitness: " + str(self.fitness) + '\n' + "Error: " + str(self.error)


def generate_initial_population(P, fitness, random_min, random_max):
    population = []
    i = 0

    while i < P:
        genotype = np.random.uniform(random_min, random_max, 11)
        aux, error = fitness(genotype)
        X = Individual(genotype, aux, error)
        population.append(X)
        i += 1

    return population
