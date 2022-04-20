import json
import sys
import time

from TP2.util.crossover import simple_crossover, uniform_crossover, multiple_crossover
from TP2.populations.population_0 import generate_initial_population
from TP2.populations.next_population import create_next_population
from TP2.util.function import error
from TP2.util.selection import elite_selection, roulette_wheel_selection, rank_selection, boltzmann_selection, \
    tournament_selection, truncated_selection, sort_population_by_fitness

import matplotlib.pyplot as plt

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
    if P % 2 != 0:
        P = P + 1

    random_min = config['random_min']
    random_max = config['random_max']
    accepted_solution = config['accepted_solution']
    k = config['k']
    tc = config['tc']
    to = config['to']

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

    print("Generations =", generations)
    print("Population =", P)
    print("Accepted solution=", accepted_solution)
    print("Mutation probability =", mutation_p)
    print('Mutation interval = [' + str(-mutation_a) + ', ' + str(mutation_a) + ']')
    print("Crossing method =", config['crossing_method'])
    print("Selection method =", config['selection_method'])
    print("Random min =", random_min)
    print("Random max =", random_max)
    print("Points =", points)
    print("Output =", output)
    print("k =", k)
    print("tc =", tc)
    print("to =", to)

    print("\n\n--------------------------------------------------\n\n")
    print("START...\n")

    start_time = time.process_time()

    population = generate_initial_population(P, fitness, random_min, random_max)
    stop = 0
    t = 0
    best_fitness = []
    while stop == 0:
        print("Generation: ", t)
        new_population = create_next_population(population, fitness, crossing_method, mutation_p, mutation_a, P)
        new_population = sorted(new_population, key=sort_population_by_fitness, reverse=True)

        if config['selection_method'] == 'boltzmann':
            aux = selection_method(population + new_population, P, k, tc, to, t, fitness)
        elif config['selection_method'] == 'rank':
            aux = selection_method(population + new_population, P, fitness)
        elif config['selection_method'] == 'truncated':
            aux = selection_method(population + new_population, P, k)
        else:
            aux = selection_method(population + new_population, P)

        population = sorted(aux, key=sort_population_by_fitness, reverse=True)
        print("-- Best individual --")
        print(population[0])
        print("\n")
        if population[0].fitness >= accepted_solution or t > generations:
            print("STOP\n")
            print("-- Best Solution --")
            print(population[0])
            stop = 1
            end_time = time.process_time()
            print('Tiempo: ', end_time - start_time)
        t = t + 1
        best_fitness.append(population[0].fitness)

    return best_fitness


def main():
    # -- Graphics --
    fig, ax = plt.subplots()
    ax.set_title("Relationship between error and generations - " + config['selection_method'] + " selection")
    ax.set_xlabel("Generations")
    ax.set_ylabel("Error")
    # plt.ylim(0,3)

    for i in range(10):
        ax.plot(algorithm(), 'C'+str(i),  label='Attempt ' + str(i))
    plt.legend()
    plt.show()
    return 0


print("Starting genetic algorithm...")
main()
print("- END -")
