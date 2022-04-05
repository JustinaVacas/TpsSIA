import math
import random
import numpy


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


def rank_selection(population, P, fitness):

    def fitness_inverse(n, total):
        return (2 * total - n) / (2 * total)

    for i in range(len(population)):
        population[i].fitness = fitness_inverse(i, 2 * P)

    population = sorted(population, key=sort_population_by_fitness, reverse=True)
    new_population = roulette_wheel_selection(population, P)
    for i in range(len(new_population)):
        new_population[i].fitness = fitness(new_population[i].genotype)
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


def boltzmann_selection(population, P, k, tc, to, t, fitness):
    T = tc + (to - tc) * math.exp(- k * t)

    def pseudo_fitness(n):
        return math.exp((fitness(population[n].genotype)) / T)

    total = 0
    for i in range(len(population)):
        total += pseudo_fitness(i)

    for j in range(len(population)):
        population[j].fitness = pseudo_fitness(j)

    new_population = roulette_wheel_selection(population, P)
    for i in range(len(new_population)):
        new_population[i].fitness = fitness(new_population[i].genotype)
    return new_population



def truncated_selection(population, P, k):
    fitness = sorted(population, key=lambda x: x.fitness)
    fitness = fitness[k:]
    return random.sample(fitness, P)
