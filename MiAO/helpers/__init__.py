from itertools import tee
import numpy as np


def memoize(f):
    memo = {}

    def helper(x):
        key = np.linalg.norm(x)
        if key not in memo:
            memo[key] = f(x)
        return memo[key]

    return helper


def pairwise(iterable, skip=1):
    a, b = tee(iterable)
    for i in range(skip):
        next(b)
    return zip(a, b)
