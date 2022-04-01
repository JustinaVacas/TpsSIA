import numpy as np


class Individual:
    def __init__(self, genotype, fitness):
        self.genotype = genotype
        self.fitness = fitness
        
    def print(self):
        print(self.genotype)
        print('Fitness:', self.fitness)


def generate_initial_population(P, fitness, random_min, random_max):
    population = []
    i = 0

    while i < P:
        genotype = np.random.uniform(random_min, random_max, 11)
        aux = fitness(genotype)
        X = Individual(genotype, aux)
        population.append(X)
        i += 1

    return population
