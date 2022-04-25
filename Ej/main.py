import json
import sys
import time

import numpy as np

from Ej.util.method import g_des

if len(sys.argv) < 2 or not str(sys.argv[1]).endswith('.json'):
    print('Invalid argument')
    exit()

with open(sys.argv[1], 'r') as configuration:
    config = json.load(configuration)

steps = config['steps']
alpha = config['alpha']

if 'points' in config and len(config['points']) == 3:
    points = config['points']
else:
    points = [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]]

if 'output' in config and config['output'] is not None:
    output = config['output']
else:
    output = [0, 1, 1]


def main():
    x = np.random.uniform(config['random_min'], config['random_max'], 11)

    stop = 0
    start_time = time.process_time()
    g_des(x, alpha, steps, points, output)

    return 0


print("Starting...")
main()
print("- END -")
