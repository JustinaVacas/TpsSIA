import math
import random

from TP2.util.function import error


def sort_population_by_fitness(individual):
    return individual.fitness


def elite_selection(population, P):
    new_population = []
    population = sorted(population, key=sort_population_by_fitness, reverse=True)
    for i in range(P):
        new_population.append(population[i])
    return new_population


def roulette_wheel_selection(population, P):
    total_fitness = 0
    probabilities = []
    selected = []
    for i in range(len(population)):
        total_fitness += population[i].fitness
    for j in range(len(population)):
        probabilities.append(population[j].fitness / total_fitness)
    aux = 0
    while aux != P:
        num = random.uniform(0, 1)
        x = 0
        for ind in range(len(population)):
            if x + 1 == len(probabilities):
                break
            if probabilities[x] < num <= probabilities[x + 1]:
                selected.append(population[ind])
                aux += 1
            x += 1
    return selected


def roulette_wheel(population, P):
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


def rank_selection(population):
    new_population = []
    rank = list()
    for i in range(len(population)):
        rank.append([population[i], population[i].fitness])
    rank = sorted(rank, key=lambda ranking: ranking[1], reverse=True)
    f = 0
    for j in range(1, len(rank) + 1):
        f += (j - rank[j - 1][1]) / j
    for pi in range(1, len(rank) + 1):
        p = ((pi - rank[pi - 1][1]) / pi) / f
        new_population.append([rank[pi][0], p])
    return roulette_wheel(new_population, len(new_population) // 2)


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
        population.remove(aux)

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
        new_population.append([[population[j]], ve])
    return roulette_wheel_boltzmann(new_population, len(population) // 2)


def truncated_selection(population, P, k):
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
