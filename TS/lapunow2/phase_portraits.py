from collections import namedtuple

import numpy as np
from scipy.integrate import ode

from helpers import pairwise

Arrow = namedtuple('Arrow', ['x', 'y', 'len_x', 'len_y'])


def get_plot_arrows(xs, ys, n=3):
    length = 0
    for (prev_x, prev_y), (x, y) in pairwise(zip(xs, ys)):
        length += np.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
    distance, i, arrows = 0, 1, []
    for (prev_x, prev_y), (x, y) in pairwise(zip(xs, ys)):
        distance += np.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
        if distance > i * length / n:
            arrows.append(Arrow(prev_x, prev_y, x - prev_x, y - prev_y))
            i += 1
    return arrows


def trajectory(x0, derivative, bounds=lambda x: True, time=100, reverse=False):
    solver = ode(derivative).set_integrator('zvode', method='bdf')
    solver.set_initial_value(x0, 0)
    dt, points = 0.01, [x0]
    while solver.successful() and abs(solver.t) < time:
        point = solver.integrate(solver.t + dt if not reverse else solver.t - dt)
        points.append(np.real(point))
        if not bounds(point):
            break
    if reverse:
        points.reverse()
    return points
