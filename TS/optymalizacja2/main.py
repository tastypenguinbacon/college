from itertools import tee

import numpy as np
from control import tf, step
from scipy.optimize import minimize

from plot import Plot, PlotData, grid, title

def sum_of_squares(elements, dt):
    return np.sum(np.array(elements) ** 2 * dt)

def sum_of_squares_weighted(elements, dt):
    begin, end = 0, dt * (len(elements) - 1)
    time = np.linspace(begin, end, len(elements))
    squares = np.array(elements) ** 2
    return np.sum(squares * time * dt)

def overregulation(elements, dt):
    return abs(min(elements))

def regulation_time(elements, dt): 
    for index, el in reversed(list(enumerate(elements))):
        if abs(el) > 0.05:
            return (index + 1) * dt
    return 0

print(regulation_time([0, 0.01, 0.02, 0.06, 0.05, 0.04, 0.03, 0.02], 0.1))
