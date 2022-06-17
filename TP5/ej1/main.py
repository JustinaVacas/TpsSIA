#Ej1-a

from typing import List
import numpy as np
from TP5.ej1.util.autoencoder_utils import to_bits, labeled_scatter, print_bit_array, generate
from TP5.fonts import font2, font2_lables, font1, font1_lables, font3_lables, font3
from TP5.ej1.util.multiple_perceptron import Network

import os
import sys

basePath = '..'

module_path = os.path.abspath(os.path.join(basePath))
if module_path not in sys.path:
    sys.path.append(module_path)

training_points = to_bits(font3)

layers: List[int] = [25,15,5, 2, 5,15,25]
layers.append(np.size(training_points, axis=1))
layers.insert(0, np.size(training_points, axis=1))

epoch = 5000
eta = 0.0005

neural_network: Network = Network(np.size(training_points, 1), layers, np.size(training_points, 1), 1e-6)

count = 35
start = 0
training_points = training_values = to_bits(font3)[start:start+count]

neural_network.train(training_points, training_values, epoch, eta,5, 0.5,10, 0.1, True)