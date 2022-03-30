import random
import numpy
from TP2.population_0 import Individual


def elite_selection(population):
    max_fitness = 0
    for i in range(len(population)):
        if i != 0:
            if population[max_fitness].fitness < population[i].fitness:
                max_fitness = i
    return population[max_fitness]


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
            if probabilities[x] < num < probabilities[x + 1]:
                selected.append(population[ind])
                break
            x += 1
    return selected[0]


def rank_selection(population):
    '''
    fitness = list()
    for i in range(len(population)):
        fitness.append(population[i])
    fitness.sort(key=lambda x: x.fitness, reverse=True)
    '''
    return population


def tournament_selection(population):
    return population


def boltzmann_selection(population):
    return population


def truncated_selection(population, k):
    fitness = sorted(population, key=lambda x: x.fitness)
    fitness = fitness[k:]
    return random.sample(fitness, 1)[0].fitness  # cuantos selecciona aleatoriamente


individual1 = Individual(numpy.random.uniform(-1000, 1000, 11), 1)
individual2 = Individual(numpy.random.uniform(-1000, 1000, 11), 2)
individual3 = Individual(numpy.random.uniform(-1000, 1000, 11), 3)
individual4 = Individual(numpy.random.uniform(-1000, 1000, 11), 4)
population = [individual1, individual2, individual3, individual4]
print("truncada: ", truncated_selection(population, 2))
