import itertools

import numpy as np
from numpy.ma import sqrt

from helpers import pairwise, validate


class Expansion(object):
    def __init__(self, fun):
        self._fun = fun

    def __call__(self, x0, direction, alpha, step_size=0.01):
        direction /= np.linalg.norm(direction)
        curr_pt = x0
        yield x0
        for i in itertools.count():
            next_pt = x0 + step_size * direction * alpha ** i
            yield next_pt
            if self._fun(curr_pt) < self._fun(next_pt):
                return
            curr_pt = next_pt

    @staticmethod
    def trim(solution, max_iterations):
        y = None
        for i, (x, y) in enumerate(pairwise(solution)):
            if i >= max_iterations:
                break
            yield x
        else:
            if y is not None:
                yield y


def valid(__, range_begin, range_end, accuracy):
    assert len(list(np.shape(range_begin))) <= 1
    assert len(list(np.shape(range_end))) <= 1
    assert len(list(np.shape(accuracy))) == 0


class GoldenRatio(object):
    _tau = (sqrt(5) - 1) / 2

    def __init__(self, fun):
        self._fun = fun

    @validate(valid)
    def __call__(self, range_begin, range_end, accuracy):
        yield range_begin
        yield range_end
        while True:
            span = range_end - range_begin
            if np.linalg.norm(span) < accuracy:
                break
            left, right = range_begin + span * (1 - self._tau), range_begin + span * self._tau
            if self._fun(left) < self._fun(right):
                yield left
                range_end = right
            else:
                yield right
                range_begin = left


def valid(this, x0, direction):
    assert len(list(np.shape(x0.shape))) <= 1
    assert len(list(np.shape(direction.shape))) <= 1


class Directional(object):
    def __init__(self, fun):
        self._golden_ratio = GoldenRatio(fun)
        self._expansion = Expansion(fun)

    @validate(valid)
    def __call__(self, x0, direction):
        in_direction = Expansion.trim(self._expansion(x0, direction / 1000, 2), 100)
        in_direction = list(in_direction)
        if len(in_direction) > 2:
            begin, end = in_direction[-3], in_direction[-1]
        else:
            begin, end = in_direction[0], in_direction[1]
        solution = self._golden_ratio(begin, end, 10e-10)

        return (list(solution))[-1]
