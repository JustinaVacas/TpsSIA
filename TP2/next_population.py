import random
from population_0 import Individual


def select(population, i):
    return population[i], population[i + 1]


def mutate(x, p, a):
    for i in range(len(x)):
        if random.uniform(0, 1) > p:
            r = random.uniform(-a, a)
            x[i] = x[i] + r
    print(x)


def create_next_population(population, fitness, crossing_method, mutation_p, mutation_a, P):
    i = 0
    new_population = []
    while i < P:
        x1, x2 = select(population, 2 * i)
        n1, n2 = crossing_method(x1.genotype, x2.genotype)
        mutate(n1, mutation_p, mutation_a)
        mutate(n2, mutation_p, mutation_a)
        new_population.append(Individual(n1, fitness(n1)))
        new_population.append(Individual(n2, fitness(n1)))

    return new_population
