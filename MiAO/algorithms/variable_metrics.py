from itertools import count

import numpy as np

from algorithms.directional import Directional
from helpers import validate


class VariableMetrics(object):
    def __init__(self, fun, grad):
        self._fun = fun
        self._grad = grad

    def __call__(self, x0):
        renew_rate = 2 * len(x0)
        x, x_prev, improved = np.array(x0), np.array(x0), False
        inv_hessian = np.eye(len(x0))
        for i in count():
            yield x
            if i % renew_rate == 0 or not improved:
                inv_hessian = np.eye((len(x0)))
            else:
                inv_hessian = self._get_metrics(x, x_prev, inv_hessian)
            direction = -inv_hessian @ self._grad(x)
            if np.dot(direction, self._grad(x)) < 0:
                solver = Directional(self._fun)
                x, x_prev = solver(x, direction), x
                improved = True
            else:
                improved = False

    def _get_metrics(self, x, x_prev, inv_hessian):
        pass

    def trim(self, intermediate_points, gradient_limit=0.001):
        for point in intermediate_points:
            if np.linalg.norm(self._grad(point)) > gradient_limit:
                yield point
            else:
                yield point
                break

    @staticmethod
    def validate(__, x, x_prev, inv_hessian):
        assert len(x.shape) == 1
        assert len(x_prev.shape) == 1
        assert len(inv_hessian) == 2


class DavidonFletcherPowell(VariableMetrics):
    @validate(validator=VariableMetrics.validate)
    def _get_metrics(self, x, x_prev, inv_hessian):
        diff = np.array([x - x_prev]).T
        g_diff = np.array([self._grad(x) - self._grad(x_prev)]).T
        temp = inv_hessian @ g_diff
        return (inv_hessian + diff @ diff.T /
                (g_diff.T @ diff) - temp @ temp.T /
                (g_diff.T @ temp))


class WolfeBroydenDavidon(VariableMetrics):
    @validate(validator=VariableMetrics.validate)
    def _get_metrics(self, x, x_prev, inv_hessian):
        diff = np.array([x - x_prev]).T
        g_diff = np.array([self._grad(x) - self._grad(x_prev)]).T
        temp = inv_hessian @ g_diff
        temp = diff - temp
        return inv_hessian + temp @ temp.T / (temp.T @ g_diff)


class BroydenFletcherGoldfarbShanno(VariableMetrics):
    @validate(validator=VariableMetrics.validate)
    def _get_metrics(self, x, x_prev, inv_hessian):
        g_diff = np.array([self._grad(x) - self._grad(x_prev)]).T
        diff = np.array([x - x_prev]).T
        temp0 = inv_hessian @ g_diff
        temp1 = diff.T @ g_diff
        temp2 = temp0 @ diff.T
        return (inv_hessian + (1 + g_diff.T @ temp0 / temp1) *
                diff @ diff.T) / temp1 - (temp2 + temp2.T) / temp1


class Pearson1(VariableMetrics):
    @validate(validator=VariableMetrics.validate)
    def _get_metrics(self, x, x_prev, inv_hessian):
        g_diff = np.array([self._grad(x) - self._grad(x_prev)]).T
        temp = inv_hessian @ g_diff
        return inv_hessian - temp * temp.T / (temp.T * g_diff)


class Pearson2(VariableMetrics):
    @validate(validator=VariableMetrics.validate)
    def _get_metrics(self, x, x_prev, inv_hessian):
        diff = np.array([x - x_prev]).T
        g_diff = np.array([self._grad(x) - self._grad(x_prev)]).T
        temp0 = inv_hessian @ g_diff
        temp1 = diff - temp0
        return inv_hessian + temp1 @ temp0.T / (temp0.T @ g_diff)


class McCromick(VariableMetrics):
    @validate(validator=VariableMetrics.validate)
    def _get_metrics(self, x, x_prev, inv_hessian):
        diff = np.array([x - x_prev]).T
        g_diff = np.array([x - x_prev]).T
        temp0 = inv_hessian @ g_diff
        temp1 = diff.T @ g_diff
        temp2 = diff - temp0
        return inv_hessian + temp2 @ diff.T / temp1
