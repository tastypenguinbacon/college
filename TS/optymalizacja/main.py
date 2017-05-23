from itertools import tee

import numpy as np
from control import tf, step
from scipy.optimize import minimize

from plot import Plot, PlotData, grid, title

day_of_birth = 11
month_of_birth = 8


def trim(min_limit, max_limit):
    def wrapper(func):
        def wrapped(*args):
            result = func(*args)
            if result < min_limit: return min_limit
            if result > max_limit: return max_limit
            return result

        return wrapped

    return wrapper


def error_output(k, t_i, t_d, dt=0.1):
    if k < 0 or t_i < 0 or t_d < 0:
        return [2.0 ** 63, 2.0 ** 63], [1, 1]
    open_system = tf([1], [1 / day_of_birth, 1]) ** month_of_birth
    t = np.arange(0, 10, step=dt)
    error_transfer_function = 1 / (1 + open_system * pid(k, t_i, t_d))
    return step(error_transfer_function, T=t)


def pid(k, t_i, t_d):
    P = tf([1], [1])
    k, t_i, t_d = float(k), float(t_i), float(t_d)
    I = tf([1], [t_i, 0]) if t_i != 0 else tf([0], [1])
    D = tf([t_d, 0], [1])
    return k * (P + I + D)


@trim(0, 2 ** 32)
def square_integral(x):
    return sum(np.array(error_output(x[0], x[1], x[2])[0]) ** 2) * 0.1


@trim(0, 2 ** 32)
def abs_integral(x):
    return sum(np.abs(np.array(error_output(x[0], x[1], x[2])[0]))) * 0.1


@trim(0, 2 ** 32)
def linear(x):
    y, t = error_output(x[0], x[1], x[2])
    y, t = np.array(y), np.array(t)
    return sum(t * y * (y * 0.1))


@trim(0, 2 ** 32)
def nothing_added(x):
    return sum(np.array(error_output(x[0], x[1], x[2])[0]) * 0.1)


def pairwise(x):
    x, y = tee(x)
    next(y)
    return zip(x, y)


@trim(0, 2 ** 32)
def with_rate_change(x):
    y = error_output(x[0], x[1], x[2])[0]
    derivative_sum = 0
    for prev, curr in pairwise(iter(y)):
        derivative_sum += ((curr - prev) / 0.1) ** 2
    return derivative_sum * 0.1 + sum(np.array(y) ** 2 * 0.1)


cumulative_plot = Plot(1, 1)
cumulative_plot.decorate_subplot(1, 1, grid(True))
cumulative_plot.decorate_subplot(1, 1, title("Porównanie wskaźników"))


def minimize_and_plot(fun, file_name='tex/svg/cudo.svg', label='', method=None):
    minimum = minimize(fun, np.array([0.5, 0.5, 0.5]), method=method)
    print(minimum)
    assert minimum.success
    x_min = minimum.x
    y, t = error_output(x_min[0], x_min[1], x_min[2], dt=0.01)
    print(square_integral((x_min[0], x_min[1], x_min[2])))
    plt = Plot(1, 1)
    plt.decorate_subplot(1, 1, title("$k=%0.3f$, $T_i$=%0.3f, $T_d$=%0.3f" % (x_min[0], x_min[1], x_min[2])))
    plt.plot(1, 1, PlotData(t, y)).decorate_subplot(1, 1, grid(True)).save(file_name)
    cumulative_plot.plot(1, 1, PlotData(t[0:len(t) // 2], y[0:len(t) // 2]), label=label)


minimize_and_plot(square_integral, file_name='tex/svg/square.svg', label='$\\int_0^\\infty e^2(t) \\mathrm{d}t$')
minimize_and_plot(abs_integral, file_name='tex/svg/abs.svg', method='Powell',
                  label='$\\int_0^\\infty |e(t)| \\mathrm{d}t$')
minimize_and_plot(linear, file_name='tex/svg/linear.svg', label='$\\int_0^\\infty te^2(t) \\mathrm{d}t$')
minimize_and_plot(with_rate_change, file_name='tex/svg/rate_change.svg',
                  label='$\\int_0^\\infty e^2(t) + \\dot{e}^2(t) \\mathrm{d}t$')

cumulative_plot.decorate_subplot(1, 1, lambda x: x.legend(loc='lower right', prop={'size': 6}))
cumulative_plot.save('tex/svg/cumulative.svg').show()
