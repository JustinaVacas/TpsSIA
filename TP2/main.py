import json
import sys
import numpy as np

from crossover import simple_crossover, uniform_crossover, multiple_crossover
from population_0 import generate_initial_population
from next_population import create_next_population
from function import error
from selection import elite_selection, roulette_wheel_selection, rank_selection, boltzmann_selection, \
    tournament_selection, truncated_selection

if len(sys.argv) < 2 or not str(sys.argv[1]).endswith('.json'):
    print('Invalid argument')
    exit()

with open(sys.argv[1], 'r') as configuration:
    config = json.load(configuration)


def algorithm():
    generations = config['generations']
    mutation_p = config['mutation_p']
    mutation_a = config['mutation_a']

    # Default 'simple'
    crossing_method = simple_crossover
    if 'crossing_method' in config:
        if config['crossing_method'] == 'simple':
            crossing_method = simple_crossover
        elif config['crossing_method'] == 'multiple':
            crossing_method = multiple_crossover
        elif config['crossing_method'] == 'uniform':
            crossing_method = uniform_crossover

    # Default 'elite'
    selection_method = elite_selection
    if 'selection_method' in config:
        if config['selection_method'] == 'elite':
            selection_method = elite_selection
        if config['selection_method'] == 'roulette':
            selection_method = roulette_wheel_selection
        if config['selection_method'] == 'rank':
            selection_method = rank_selection
        if config['selection_method'] == 'tournament':
            selection_method = tournament_selection
        if config['selection_method'] == 'boltzmann':
            selection_method = boltzmann_selection
        if config['selection_method'] == 'truncated':
            selection_method = truncated_selection

    P = config['P']
    random_min = config['random_min']
    random_max = config['random_max']
    accepted_solution = config['accepted_solution']

    if 'points' in config and len(config['points']) == 3:
        points = config['points']
    else:
        points = [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]]

    if 'output' in config and config['output'] is not None:
        output = config['output']
    else:
        output = [0, 1, 1]

    def fitness(individual):
        return error(individual, output, points)

    def sort_population_by_fitness(individual):
        return individual.fitness

    print("Generations = ", generations)
    print("Mutation probability = ", mutation_p)
    print('Mutation interval = [', -mutation_a, ',', mutation_a, ']')
    print("Crossing_method = ", crossing_method)
    print("Population = ", P)
    print("Random_min = ", random_min)
    print("Random_max = ", random_max)
    print("Points = ", points)
    print("Output = ", output)

    population = generate_initial_population(P, fitness, random_min, random_max)
    population = sorted(population, key=sort_population_by_fitness)
    stop = 0
    t = 0
    while stop == 0:
        print("Generation: ", t)
        new_population = create_next_population(population, fitness, crossing_method, mutation_p, mutation_a, P)
        aux = selection_method(np.append(population, new_population))
        population = sorted(aux, key=sort_population_by_fitness)
        print("Best fitness individual: ", population[0])
        if population[0].fitness < accepted_solution or t > 500:
            print("Algorithm stopped")
            stop = 1
        t = t+1
    return 0


print("Starting genetic algorithm...")
algorithm()
print("- End -")
