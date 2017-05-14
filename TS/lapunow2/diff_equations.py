import numpy as np


def first_system(x):
    x1, x2 = x[0], x[1]
    return np.array([
        -x1 + 2 * x1 ** 2 * x2,
        -x2
    ])


def pendulum(y, a, b):
    y1 = y[1]
    y2 = -b * y[1] - a * np.sin(y[0])
    return np.array([y1, y2])


def get_jacobian_for_point(x, fun):
    delta = 0.0001
    a11 = (fun(0, x + np.array([delta, 0]) - fun(0, x)))[0] / delta
    a12 = (fun(0, x + np.array([0, delta]) - fun(0, x)))[0] / delta
    a21 = (fun(0, x + np.array([delta, 0]) - fun(0, x)))[1] / delta
    a22 = (fun(0, x + np.array([0, delta]) - fun(0, x)))[1] / delta
    A = np.array([[a11, a12],
                  [a21, a22]])
    print(A)
    return A


def linear_form(y, A):
    return A @ y
