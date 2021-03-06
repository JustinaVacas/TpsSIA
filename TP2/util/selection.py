import math
import random


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
        probabilities = []
        total_fitness = sum([c.fitness for c in population])
        for j in range(len(population)):
            probabilities.append([population[j], population[j].fitness / total_fitness])
        num = random.uniform(0, 1)
        current = 0
        for i in probabilities:
            current += i[1]
            if current > num:
                selected.append(i[0])
                population.remove(i[0])
                break
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
        new_population[i].fitness, new_population[i].error = fitness(new_population[i].genotype)
    return new_population


def tournament_select(population):
    u = random.uniform(0.5, 1)
    points = random.sample(range(1, len(population)), 4)
    i = 0
    while i < 6:
        r = random.uniform(0, 1)
        if r < u:  # selecciono el mas apto
            if population[points[i]].fitness > population[points[i + 1]].fitness:
                points.append(points[i])
            else:
                points.append(points[i + 1])
        else:  # selecciono el menos apto
            if population[points[i]].fitness > population[points[i + 1]].fitness:
                points.append(points[i + 1])
            else:
                points.append(points[i])
        i += 2
    return population[points[6]]


def tournament_selection(population, P):
    new_population = []
    for i in range(P):
        aux = tournament_select(population)
        new_population.append(aux)
        population.remove(aux)

    return new_population


def boltzmann_selection(population, P, k, tc, to, t, fitness):
    T = tc + (to - tc) * math.exp((-k) * t)

    def pseudo_fitness(n):
        f, error = fitness(population[n].genotype)
        return math.exp(f / T)

    total = 0
    for i in range(len(population)):
        total += pseudo_fitness(i)

    for j in range(len(population)):
        population[j].fitness = pseudo_fitness(j)

    new_population = roulette_wheel_selection(population, P)
    for i in range(len(new_population)):
        new_population[i].fitness, new_population[i].error = fitness(new_population[i].genotype)
    return new_population


def truncated_selection(population, P, k):
    population = sorted(population, key=sort_population_by_fitness)
    population = population[k:]
    return random.sample(population, P)
