from itertools import count

import numpy as np

from algorithms.directional import Directional
from helpers import validate


def call_validator(__, x0):
    assert len(x0.shape) == 1


def beta_validator(__, x, x_prev, direction):
    assert len(x.shape) == 1
    assert len(x_prev.shape) == 1
    assert len(direction.shape) == 1


class GradientMethod(object):
    def __init__(self, fun, grad):
        self._fun = fun
        self._grad = grad

    @validate(call_validator)
    def __call__(self, x0):
        renew_rate = 2 * len(x0)
        x, x_prev, direction, improved = np.array(x0), np.array(x0), 0, False
        for i in count():
            yield x
            g = self._grad(x)
            if i % renew_rate == 0 or not improved:
                direction = -g
            else:
                beta = self._get_beta(x, x_prev, direction)
                direction = -g + beta * direction
            if np.dot(direction, g) < 0:
                directional = Directional(self._fun)
                x, x_prev = directional(x, direction), x
                improved = True
            else:
                improved = False

    def _get_beta(self, x, x_prev, direction) -> float:
        pass

    def trim(self, intermediate_points, gradient_limit=0.001):
        for point in intermediate_points:
            if np.linalg.norm(self._grad(point)) > gradient_limit:
                yield point
            else:
                yield point
                break


class FastestDescending(GradientMethod):
    @validate(beta_validator)
    def _get_beta(self, x, x_prev, direction):
        return 0


class FletcherReeves(GradientMethod):
    @validate(beta_validator)
    def _get_beta(self, x, x_prev, direction):
        g = self._grad(x)
        g_prev = self._grad(x_prev)
        x = np.linalg.norm(g) ** 2
        x_prev = np.linalg.norm(g_prev) ** 2
        return x / x_prev


class PolakRibiere(GradientMethod):
    @validate(beta_validator)
    def _get_beta(self, x, x_prev, direction):
        g = self._grad(x)
        g_prev = self._grad(x_prev)
        x_prev = np.linalg.norm(g_prev) ** 2
        return (np.dot(g, g - g_prev) /
                x_prev)


class FullBetaFormula(GradientMethod):
    @validate(beta_validator)
    def _get_beta(self, x, x_prev, direction):
        g = self._grad(x)
        g_prev = self._grad(x_prev)
        g_diff = g - g_prev
        return (np.dot(g, g_diff) /
                np.dot(direction, g_diff))
