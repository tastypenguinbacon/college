from itertools import islice

import matplotlib.pyplot as plt
import numpy as np

from algorithms.gradient import FastestDescending, FletcherReeves, PolakRibiere, FullBetaFormula


def function(x):
    return x @ np.array([[1, 0], [0, 3]]) @ x


def gradient(x):
    return 2 * np.array([[1, 0], [0, 3]]) @ x


solvers = [
    FastestDescending(function, gradient),
    FletcherReeves(function, gradient),
    PolakRibiere(function, gradient),
    FullBetaFormula(function, gradient)
]
for fd in solvers:
    x0 = np.array([10, 10])

    fd = np.array(list(islice(fd(x0, 10), 0, 20)))
    plt.plot(fd[:, 0], fd[:, 1])

plt.show()
