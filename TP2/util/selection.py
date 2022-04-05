import math
import random
import numpy

from TP2.util.function import error
from TP2.populations.population_0 import Individual


def sort_population_by_fitness(individual):
    return individual.fitness


def elite_selection(population, P):
    new_population = []
    population = sorted(population, key=sort_population_by_fitness, reverse=True)
    for i in range(P):
        new_population.append(population[i])
    return new_population


def roulette_wheel_selection(population, P):
    selected = []
    aux = 0
    while aux < P:
        total_fitness = 0
        probabilities = []
        for i in range(len(population)):
            total_fitness += population[i].fitness
        for j in range(len(population)):
            probabilities.append(population[j].fitness / total_fitness)
        num = random.uniform(0, 1)
        x = 0
        while x < len(probabilities) and probabilities[x] <= num:
            x += 1
        if x == 0:
            x = 1
        selected.append(population[x - 1])
        population = numpy.delete(population, x - 1)
        aux += 1

    return selected


def roulette_wheel(population, P):
    selected = []
    aux = 0
    while aux < P:
        total_fitness = 0
        probabilities = []
        for i in range(len(population)):
            total_fitness += population[i][1]
        for j in range(len(population)):
            probabilities.append(population[j][1] / total_fitness)
        num = random.uniform(0, 1)
        x = 0
        while x < len(probabilities) and probabilities[x] <= num:
            x += 1
        if x == 0:
            x = 1

        selected.append(population[x - 1][0])
        new_population = []
        for i in range(len(population)):
            if i != (x - 1):
                new_population.append(population[i])
        population = new_population
        aux += 1
    return selected


def rank_selection(population, P):

    def fitness_inverse(n, total):
        return (2 * total - n) / (2 * total)

    for i in range(len(population)):
        population[i].fitness = fitness_inverse(i, 2 * P)

    population = sorted(population, key=sort_population_by_fitness, reverse=True)
    new_population = roulette_wheel_selection(population, P)
    return new_population


def tournament_select(population):
    u = random.uniform(0.5, 1)
    points = random.sample(range(1, len(population)), 4)
    r = random.uniform(0, 1)
    p = []
    for i in range(0, 3, 2):
        if r < u:  # selecciono el mas apto
            if population[points[i]].fitness > population[points[i + 1]].fitness:
                p.append(population[points[i]])
            else:
                p.append(population[points[i + 1]])
        else:  # selecciono el menos apto
            if population[points[i]].fitness > population[points[i + 1]].fitness:
                p.append(population[points[i + 1]])
            else:
                p.append(population[points[i]])
    if p[0].fitness > p[1].fitness:
        return p[0]
    return p[1]


def tournament_selection(population, P):
    new_population = []
    for i in range(P):
        aux = tournament_select(population)
        new_population.append(aux)
        new_pop = []
        for i in range(len(population)):
            if population[i] != aux:
                new_pop.append(population[i])
        population = new_pop

    return new_population


def roulette_wheel_boltzmann(population, P):
    total_fitness = 0
    probabilities = []
    selected = []
    for i in range(len(population)):
        total_fitness += population[i][1]
    for j in range(len(population)):
        probabilities.append(population[j][1] / total_fitness)
    for p in range(P):
        num = random.uniform(0, 1)
        x = 0
        for ind in range(len(population)):
            if x + 1 == len(probabilities):
                break
            if probabilities[x] < num <= probabilities[x + 1]:
                selected.append(population[ind])
            x += 1
    return selected


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
        new_population.append([population[j], ve])
    return roulette_wheel(new_population, len(population) // 2)


def truncated_selection(population, P, k):
    fitness = sorted(population, key=lambda x: x.fitness)
    fitness = fitness[k:]
    return random.sample(fitness, P)

# individual1 = Individual(numpy.random.uniform(-10, 10, 11), 1)
# individual2 = Individual(numpy.random.uniform(-10, 10, 11), 2)
# individual3 = Individual(numpy.random.uniform(-10, 10, 11), 3)
# individual4 = Individual(numpy.random.uniform(-10, 10, 11), 4)
# individual5 = Individual(numpy.random.uniform(-10, 10, 11), 5)
# individual6 = Individual(numpy.random.uniform(-10, 10, 11), 6)
# individual7 = Individual(numpy.random.uniform(-10, 10, 11), 7)
# individual8 = Individual(numpy.random.uniform(-10, 10, 11), 8)
# individual9 = Individual(numpy.random.uniform(-10, 10, 11), 9)
# individual10 = Individual(numpy.random.uniform(-10, 10, 11), 10)
# population = [individual1, individual2, individual3, individual4, individual5, individual6, individual7, individual8,
#               individual9, individual10]
# print("ranking ", rank_selection(population, len(population) // 2))
# print("boltzmann ", boltzmann_selection(population, 1, 5, 40, 1, [0, 1, 2], [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]]))
