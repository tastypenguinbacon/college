from itertools import count, islice

import matplotlib.pyplot as plt
import numpy as np

from algorithms.gradient import FastestDescending


def gradient(function):
    d = 10e-9
    dx = np.array([d, 0])
    dy = np.array([0, d])

    def grad(x):
        up = (function(x + dx) - function(x)) / d
        down = (function(x + dy) - function(x)) / d
        return np.array([up, down])

    return grad


def function(x):
    A = np.array([
        [1, 0],
        [0, 1]
    ])
    return x.T @ A @ x


def penalty_function(x):
    x1, x2 = x[0], x[1]
    return np.exp((x2 - 1) ** 2)


def penalize(i):
    return lambda x: function(x) + i * penalty_function(x) / 10


def solver():
    for i in count():
        solv = FastestDescending(penalize(i), gradient(penalize(i)))
        yield list(solv.trim(solv(np.array([-3, 3]))))


cudo = list(islice(map(lambda p: p[-1], solver()), 0, 1000))
x = list(map(lambda array: array[0], cudo))
y = list(map(lambda array: array[1], cudo))

plt.plot(x, y, 'C3+')
plt.grid(True)
plt.show()
