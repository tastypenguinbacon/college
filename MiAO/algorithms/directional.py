import itertools

import numpy as np
from numpy.ma import sqrt

from helpers import memoize, pairwise


class Expansion(object):
    def __init__(self, fun):
        self._fun = memoize(fun)

    def __call__(self, x0, direction, alpha):
        curr_pt = x0
        yield x0
        for i in itertools.count():
            next_pt = x0 + direction * alpha ** i
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


class GoldenRatio(object):
    _tau = (sqrt(5) - 1) / 2

    def __init__(self, fun):
        self._fun = memoize(fun)

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


class Directional(object):
    def __init__(self, fun):
        self._golden_ratio = GoldenRatio(fun)
        self._expansion = Expansion(fun)

    def __call__(self, x0, direction):
        in_direction = Expansion.trim(self._expansion(x0, direction, 2), 100)
        in_direction = list(in_direction)
        if len(in_direction) > 2:
            begin, end = in_direction[-3], in_direction[-1]
        else:
            begin, end = in_direction[0], in_direction[1]
        solution = self._golden_ratio(begin, end, 10e-5)
        cudo = (list(solution))
        return cudo[-1]


if __name__ == '__main__':
    cudo = Directional(lambda x: x ** 2)
    dirr = Expansion(lambda x: x ** 2)
    print(cudo(10, -1))
