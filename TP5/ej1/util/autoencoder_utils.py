import numpy as np
from matplotlib import pyplot as plt


def labeled_scatter(xValues, yValues, labels=None):
    plt.figure(figsize=(16, 10))
    xs = xValues
    ys = yValues

    plt.scatter(xs, ys)

    for i in range(len(labels)):
        plt.text(xs[i], ys[i], s=labels[i],
                 fontdict=dict(color='red', size=10))

    plt.xlabel("X")
    plt.xlabel("Y")
    plt.grid()
    plt.show()


def to_bits(values: np.ndarray) -> np.ndarray:
    new_values = np.empty((np.size(values, 0), np.size(values, 1) * 5))

    for i in range(np.size(values, 0)):
        new_values[i] = np.array([[(1 if (v >> i & 1) == 1 else -1) for i in range(4, -1, -1)] for v in values[i]]).flatten()

    return new_values


def add_noise(images: np.ndarray, noise: float):
    images_with_noise = []
    for image in images:
        images_with_noise.append(np.array([image[i] - np.random.uniform(0.1, 0.2)*image[i]
                                           if np.random.random() < noise else image[i] for i in range(np.size(image))]))

    return np.array(images_with_noise)

