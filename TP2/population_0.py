import numpy


class individual:
    def __init__(self, genotype, fitness):
        self.genotype = genotype
        self.fitness = fitness
        
    def print(self):
        print(self.genotype)
        print('Fitness:', self.fitness)


def generate_initial_population():
    P = 1000
    population = []
    i = 0

    while i < P:
        genotype = numpy.random.uniform(-1000, 1000, 11)
        fitness = 0
        X = individual(genotype, fitness)
        population.append(X)
        i += 1

    return population
