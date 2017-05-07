from itertools import count

import numpy as np

from algorithms.directional import Directional
from helpers import memoize


class GradientMethod(object):
    def __init__(self, fun, grad):
        self._fun = memoize(fun)
        self._grad = memoize(grad)

    def __call__(self, x0, renew_rate):
        current, previous, direction, improved = np.array(x0), np.array(x0), 0, False
        for i in count():
            yield current
            gradient = self._grad(current)
            if i % renew_rate == 0 or improved:
                direction = -gradient
            else:
                beta = self._get_beta(current, previous, direction)
                direction = -gradient + beta * direction
            if np.dot(direction, gradient) < 0:
                directional = Directional(self._fun)
                current, previous = directional(current, direction), current
                improved = True
            else:
                improved = False

    def _get_beta(self, current, previous, direction) -> float:
        pass


class FastestDescending(GradientMethod):
    def _get_beta(self, current, previous, direction):
        return -self._grad(current)


class FletcherReeves(GradientMethod):
    def _get_beta(self, current, previous, direction):
        current_gradient = self._grad(current)
        previous_gradient = self._grad(previous)
        current = np.linalg.norm(current_gradient) ** 2
        previous = np.linalg.norm(previous_gradient) ** 2
        return current / previous


class PolakRibiere(GradientMethod):
    def _get_beta(self, current, previous, direction):
        current_gradient = self._grad(current)
        previous_gradient = self._grad(previous)
        previous = np.linalg.norm(previous_gradient) ** 2
        return (np.dot(current_gradient, current_gradient - previous_gradient) /
                previous)


class FullBetaFormula(GradientMethod):
    def _get_beta(self, current, previous, direction):
        current_gradient = self._grad(current)
        previous_gradient = self._grad(previous)
        difference = current_gradient - previous_gradient
        return (np.dot(current_gradient, difference) /
                np.dot(direction, difference))
