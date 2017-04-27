import numpy as np


def init_points_on_rectangle(width, height, n=30):
    angles = np.linspace(0, 2 * np.pi, n)
    starting_points = np.transpose([np.sin(angles), np.cos(angles)])
    for i in range(0, len(starting_points)):
        starting_points[i] /= np.max(np.abs(starting_points[i]))
        starting_points[i, 0] *= width / 2
        starting_points[i, 1] *= height / 2
    return starting_points


def special_init_for_negative_spring():
    xs = np.concatenate((np.linspace(-2, -1.5, 5),
                         np.linspace(-1.5, -0.9, 6),
                         np.linspace(-0.9, 0.5, 5),
                         np.linspace(0.5, 3, 5)))
    ys = np.ones(len(xs)) * 2
    xs = np.concatenate((xs, -xs))
    ys = np.concatenate((ys, -ys))
    return np.array([xs, ys]).transpose()


def corner_case_dumping_init_points(width, height):
    outer = init_points_on_rectangle(width, height, 80)
    inner = np.array([np.linspace(-width / 2, width / 2, 31),
                      np.zeros(31)]).transpose()
    return np.concatenate((outer, inner))