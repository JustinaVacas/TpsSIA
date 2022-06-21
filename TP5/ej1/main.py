#Ej1-a

from typing import List
import numpy as np
from TP5.ej1.util.autoencoder_utils import to_bits, labeled_scatter
from TP5.fonts import font2, font2_lables, font1, font1_lables, font3_lables, font3
from TP5.ej1.util.multiple_perceptron import Network

import matplotlib.pyplot as plt

import os
import sys

basePath = '..'

module_path = os.path.abspath(os.path.join(basePath))
if module_path not in sys.path:
    sys.path.append(module_path)

training_points = to_bits(font3)

layers: List[int] = [25, 15, 5, 2, 5, 15, 25]
layers.append(np.size(training_points, axis=1))
layers.insert(0, np.size(training_points, axis=1))

epoch = 5000
eta = 0.0005
noise = 0.15

neural_network: Network = Network(np.size(training_points, 1), layers, np.size(training_points, 1), 1e-6)

count = 10
start = 1
training_points = training_values = to_bits(font3)[start:start+count]

neural_network.train_with_noise(training_points, training_values, epoch, eta, noise, 5, 0.5, 10, 0.1, True)

z_values: np.ndarray = np.empty((np.size(training_points, 0), 2))
predictions: np.ndarray = np.empty(training_points.shape)

# espacio latente
for i in range(np.size(training_points, 0)):
    predictions[i], w = neural_network.predict(training_points[i])
    z_values[i] = neural_network.activations[len(layers)//2 + 1]
labeled_scatter(z_values[:, 0], z_values[:, 1], labels=font3_lables[start:start+count])

# comparar letras orginales con las predecidas
for i in range(start, start+count):
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(training_points[i].reshape(7, 5), 'gray_r')
    plt.title("Input Letter: " + font3_lables[i], fontsize=15)
    plt.xticks([])
    plt.yticks([])
    plt.subplot(1, 2, 2)
    plt.imshow(predictions[i].reshape(7, 5), 'gray_r')
    plt.title('Predicted', fontsize=15)
    plt.xticks([])
    plt.yticks([])
    plt.show()
