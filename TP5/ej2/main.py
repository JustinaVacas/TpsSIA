import keras
from keras.datasets import mnist, fashion_mnist, boston_housing
from scipy.stats import norm

# from fonts.fonts import Font3
# from utils import transform_input, letter_heatmap
from vae import VAE
# from numpy import array
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf


if __name__ == "__main__":
    layers = [256]
    max_iter = 50
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

    vae = VAE(x_train, x_train, layers, 2)

    vae.train(x_train, 5, 100)

    x_test_encoded = vae.encoder.predict(x_test, batch_size=100)[0]

    plt.figure(figsize=(6, 6))
    plt.scatter(x_test_encoded[:, 0], x_test_encoded[:, 1], c=y_test, cmap='plasma')
    plt.colorbar()
    plt.show()

    n = 15
    digit_size = 28
    figure = np.zeros((digit_size * n, digit_size * n))
    grid_x = norm.ppf(np.linspace(0.05, 0.95, n))
    grid_y = norm.ppf(np.linspace(0.05, 0.95, n))

    for i, yi in enumerate(grid_x):
        for j, xi in enumerate(grid_y):
            z_sample = np.array([[xi, yi]])
            x_decoded = vae.decoder.predict(z_sample)
            digit = x_decoded[0].reshape(digit_size, digit_size)
            figure[i * digit_size: (i + 1) * digit_size, j * digit_size: (j + 1) * digit_size] = digit

    plt.figure(figsize=(10, 10))
    plt.imshow(figure, cmap='Greys_r')
    plt.show()