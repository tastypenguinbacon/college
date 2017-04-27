import numpy as np


def van_der_poll(y, a):
    y1 = y[1] - y[0] ** 3 - 2 * a * y[0]
    y2 = -y[0]
    return np.array([y1, y2])


def mechanical_system(y, b, c, d):
    y1 = y[1]
    y2 = - b * y[1] - c * y[0] - d * y[0] ** 3
    return np.array([y1, y2])


def pendulum(y, a, b):
    y1 = y[1]
    y2 = -b * y[1] - a * np.sin(y[0])
    return np.array([y1, y2])


def get_jacobian_for_point(x, fun):
    delta = 0.001
    a11 = fun(0, x + np.array([delta, 0]))[0] / delta
    a12 = fun(0, x + np.array([0, delta]))[0] / delta
    a21 = fun(0, x + np.array([delta, 0]))[1] / delta
    a22 = fun(0, x + np.array([0, delta]))[1] / delta
    return np.array([[a11, a12],
                     [a21, a22]])


def linear_form(y, A):
    return A @ y
