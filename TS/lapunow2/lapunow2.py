import numpy as np

from helpers import MyLittleMapper
from phase_portraits import trajectory, get_plot_arrows
from plot import Plot, PlotData, title, axis, grid, plot_arrow


def function_1(t, x):
    x1, x2 = x[0], x[1]
    return np.array([
        -x1 + 2 * x1 ** 2 * x2,
        -x2
    ])


def function_2(t, x):
    x1, x2 = x[0], x[1]
    return np.array([
        x2 - x1 + x1 ** 3,
        -x1
    ])


def start_from_square():
    t = np.linspace(0, 2 * np.pi, 20)
    x, y = np.cos(t), np.sin(t)
    to_square = lambda x: np.array([x[0], x[1]]) / np.max(np.abs(x)) * 2
    return list(map(to_square, zip(x, y)))


def start_from_line():
    x = np.linspace(-0.006, 0.006, 13)
    y = np.zeros(len(x))
    return np.array([x, y]).T


def box(x):
    x1, x2 = x[0], x[1]
    return -2 <= x1 <= 2 and -2 <= x2 <= 2


# first
# first = Plot(1, 1)
# MyLittleMapper(start_from_square()) \
#     .map(lambda x: trajectory(x, function_1, bounds=box)) \
#     .map(lambda pts: (map(lambda p: p[0], pts), map(lambda p: p[1], pts))) \
#     .map(lambda x: (list(x[0]), list(x[1]))) \
#     .remember() \
#     .map(lambda x: PlotData(x[0], x[1])) \
#     .map(lambda x: first.plot(1, 1, x, 'C0')) \
#     .apply() \
#     .rewind() \
#     .map(lambda x: get_plot_arrows(x[0], x[1])) \
#     .map(lambda x: MyLittleMapper(x)
#          .map(lambda arrow: first.decorate_subplot(1, 1, plot_arrow(arrow, head_width=0.03)))) \
#     .apply()
#
# first.decorate_subplot(1, 1, grid(True)) \
#     .decorate_subplot(1, 1, title('cudo')) \
#     .decorate_subplot(1, 1, axis([-2, 2, -2, 2])) \
#     .save('holy/shit/random/cudo.svg')

# second
def limit(x):
    return (np.linalg.norm(x - np.array([1.1080954, 0])) > 0.01 and
            np.linalg.norm(x - np.array([-1.1080954, 0])) > 0.01)


second = Plot(1, 1)
MyLittleMapper(start_from_square()) \
    .map(lambda x: trajectory(x, function_2, bounds=lambda x: box(x) and limit(x), time=5, reverse=True)) \
    .map(lambda pts: (map(lambda p: p[0], pts), map(lambda p: p[1], pts))) \
    .map(lambda x: (list(x[0]), list(x[1]))) \
    .remember() \
    .map(lambda x: PlotData(x[0], x[1])) \
    .map(lambda x: second.plot(1, 1, x, 'C0')) \
    .apply().rewind() \
    .map(lambda x: get_plot_arrows(x[0], x[1])) \
    .map(lambda x: MyLittleMapper(x)
         .map(lambda arrow: second.decorate_subplot(1, 1, plot_arrow(arrow, color='C0', head_width=0.05))).apply()) \
    .apply()

MyLittleMapper(start_from_line()) \
    .map(lambda x: trajectory(x, function_2, bounds=lambda x: box(x) and limit(x), time=100, reverse=True)) \
    .map(lambda pts: (map(lambda p: p[0], pts), map(lambda p: p[1], pts))) \
    .map(lambda x: (list(x[0]), list(x[1]))) \
    .remember() \
    .map(lambda x: PlotData(x[0], x[1])) \
    .map(lambda x: second.plot(1, 1, x, 'C0')) \
    .apply().rewind() \
    .map(lambda x: get_plot_arrows(x[0], x[1])) \
    .map(lambda x: MyLittleMapper(x)
         .map(lambda arrow: second.decorate_subplot(1, 1, plot_arrow(arrow, color='C0', head_width=0.05))).apply()) \
    .apply()

second.decorate_subplot(1, 1, grid(True)) \
    .decorate_subplot(1, 1, title('cudo')) \
    .decorate_subplot(1, 1, axis([-2, 2, -2, 2])) \
    .save('holy/shit/random/cudo.svg') \
    .show()


def start_from_line():
    x = np.linspace(1.1080954, 1.1080955, 10)
    y = np.zeros(len(x))
    return np.array([x, y]).T


print(start_from_line())
