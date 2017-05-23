from operator import itemgetter

import numpy as np
from control import tf, tf2ss, nyquist
from plot import Plot, PlotData, grid


def circle(begin, end):
    middle = (end + begin) / 2
    r = (end - begin) / 2
    t = np.linspace(0, 2 * np.pi, 100)
    return r * np.cos(t) + middle, r * np.sin(t)


def all_points_in_circle(points, begin, end):
    middle = (end + begin) / 2
    r = (end - begin) / 2
    for x, y in points:
        if np.sqrt((x - middle) ** 2 + y ** 2) >= r:
            return False
    return True


# Zadanie 1

G = tf([4], [3, 1]) * tf([-5, 1], [2, 1])
ss = tf2ss(G)
A, b, c, __ = np.array(ss.A), np.array(ss.B), np.array(ss.C), np.array(ss.D)
print(A, b, c, sep='\n')

P, Q, w = nyquist([G], np.geomspace(10 ** -6, 10 ** 6, 1000), Plot=False)
P, Q, w = np.array(P), np.array(Q), np.array(w)


def search(P, Q, left_bound, right_bound):
    valid = []
    for right in np.linspace(*right_bound, 100):
        for left in np.linspace(*left_bound, 100):
            if all_points_in_circle(zip(P, Q), left, right):
                valid.append((left, right, right - left))
    valid.sort(key=itemgetter(2))
    return valid[0]


start, end, width = search(P, Q, (-4.8, -4.9), (4.0, 4.2))
print(start, end)
plt = Plot(1, 2)
(plt.plot(1, 1, PlotData(P, Q))
 .plot(1, 1, PlotData(*circle(start, end)))
 .decorate_subplot(1, 1, grid(True))
 .plot(1, 2, PlotData(P, w * Q))
 .decorate_subplot(1, 2, grid(True))
 .show())

# Zadanie 2

A = np.array([
    [-2, 1, 0],
    [-1, 0, 1],
    [-1, 0, 0]
])

b = np.array([
    [-1],
    [0],
    [0]
])

c = np.array([[1, 0, 0]])

d = np.array([[0.0]])

G = tf([-1, 0, 0], [1, 2, 1, 1])  # numerical errors happen when ss2tf(A, b, c, d)

P, Q, w = nyquist([G], np.geomspace(10 ** -6, 10 ** 6, 10000), Plot=False)
P, Q, w = np.array(P), np.array(Q), np.array(w)
plt = Plot(1, 2)
(plt.plot(1, 1, PlotData(P, Q))
 .decorate_subplot(1, 1, grid(True))
 .plot(1, 2, PlotData(P, w * Q))
 .decorate_subplot(1, 2, grid(True)))
