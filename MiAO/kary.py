from itertools import count, islice

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize


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
    return np.abs(x2 - 1) ** 2


def penalize(i):
    return lambda x: function(x) + i * penalty_function(x)


def solver():
    for i in count():
        solv = minimize(penalize(i), np.array([0, 0]), method='Powell')
        assert solv.success
        yield solv.x


cudo = list(islice(solver(), 0, 1000))
x = list(map(lambda p: p[0], cudo))
y = list(map(lambda p: p[1], cudo))
print(cudo)
plt.plot(x, y, 'C3+')
plt.axis([np.min(x), np.max(x), -1, 1.5])
plt.grid(True)
plt.show()
