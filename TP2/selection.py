import math
import random
import numpy

from TP2.function import error
from TP2.population_0 import Individual


def sort_population_by_fitness(individual):
    return individual.fitness


def elite_selection(population, P):
    new_population = []
    population = sorted(population, key=sort_population_by_fitness, reverse=True)
    for i in range(P):
        new_population.append(population[i])
    return new_population


def roulette_wheel_selection(population):
    total_fitness = 0
    probabilities = []
    selected = []
    for i in range(len(population)):
        total_fitness += population[i].fitness
    for j in range(len(population)):
        probabilities.append(population[j].fitness / total_fitness)
    while len(selected) == 0:
        num = random.uniform(0, 1)
        x = 0
        for ind in range(len(population)):
            if x + 1 == len(probabilities):
                break
            if probabilities[x] < num <= probabilities[x + 1]:
                selected.append(population[ind])
                break
            x += 1
    return Individual.print(selected[0])


def rank_selection(population):
    '''
    fitness = list()
    for i in range(len(population)):
        fitness.append(population[i])
    fitness.sort(key=lambda x: x.fitness, reverse=True)
    '''


def tournament_selection(population):
    u = random.uniform(0.5, 1)
    points = random.sample(range(1, len(population[0])), 4).sort
    r = random.uniform(0, 1)
    p = []
    for i in range(0, 3, 2):
        if r < u:  # selecciono el mas apto
            if population[i].fitness > population[i + 1]:
                p.append(population[i])
            else:
                p.append(population[i + 1])
        else:  # selecciono el menos apto
            if population[i].fitness > population[i + 1]:
                p.append(population[i + 1])
            else:
                p.append(population[i])
    if p[0].fitness > p[1].fitness:
        return p[0]
    return p[1]


def roulette_wheel_boltzmann(population):
    total_fitness = 0
    probabilities = []
    selected = []
    for i in range(len(population)):
        total_fitness += population[i][1]
    for j in range(len(population)):
        probabilities.append(population[j][1] / total_fitness)
    while len(selected) == 0:
        num = random.uniform(0, 1)
        x = 0
        for ind in range(len(population)):
            if x + 1 == len(probabilities):
                break
            if probabilities[x] < num <= probabilities[x + 1]:
                selected.append(population[ind])
                break
            x += 1
    return Individual.print(selected[0][0][0])


def boltzmann_selection(population, k, tc, to, t, output, points):
    tc = tc
    to = to
    T = tc + (to - tc) * math.exp(- k * t)
    new_population = []
    aux = 0
    for i in range(len(population)):
        aux += math.exp((error(population[i].genotype, output, points)) / T)
    for j in range(len(population)):
        ve = math.exp((error(population[j].genotype, output, points)) / T) / aux
        new_population.append([[population[j]], ve])
    return roulette_wheel_boltzmann(new_population)


def truncated_selection(population, k):
    fitness = sorted(population, key=lambda x: x.fitness)
    fitness = fitness[k:]
    return random.sample(fitness, P)
#
#
# individual1 = Individual(numpy.random.uniform(-1000, 1000, 11), 1)
# individual2 = Individual(numpy.random.uniform(-1000, 1000, 11), 2)
# individual3 = Individual(numpy.random.uniform(-1000, 1000, 11), 3)
# individual4 = Individual(numpy.random.uniform(-1000, 1000, 11), 4)
# individual5 = Individual(numpy.random.uniform(-1000, 1000, 11), 5)
# individual6 = Individual(numpy.random.uniform(-1000, 1000, 11), 6)
# individual7 = Individual(numpy.random.uniform(-1000, 1000, 11), 7)
# individual8 = Individual(numpy.random.uniform(-1000, 1000, 11), 8)
# individual9 = Individual(numpy.random.uniform(-1000, 1000, 11), 9)
# individual10 = Individual(numpy.random.uniform(-1000, 1000, 11), 10)
# population = [individual1, individual2, individual3, individual4, individual5, individual6, individual7, individual8,
#               individual9, individual10]
# roulette_wheel_selection(population, 5)
