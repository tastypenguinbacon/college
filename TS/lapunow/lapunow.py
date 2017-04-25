import os
from subprocess import call

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import ode

if not os.path.exists('tex/svg'):
    os.makedirs('tex/svg')


def van_der_poll(t, y, a):
    y1 = y[1] - y[0] ** 3 - 2 * a * y[0]
    y2 = -y[0]
    return np.array([y1, y2])


def mechanical_system(t, y, b, c, d):
    y1 = y[1]
    y2 = - b * y[1] - c * y[0] - d * y[0] ** 3
    return np.array([y1, y2])


def pendulum(t, y, a, b):
    y1 = y[1]
    y2 = -b * y[1] - a * np.sin(y[0])
    return np.array([y1, y2])


def plot(file_name, width, height):
    def plot_decorator(f):
        def wrapped(function_name, init_point_provider):
            plt.figure()
            f(function_name, init_point_provider)
            plt.axis([-width / 2, width / 2, -height / 2, height / 2])
            plt.xlabel("x1")
            plt.ylabel("x2")
            plt.savefig('tex/svg/' + file_name, bbox_inches='tight')

        return wrapped

    return plot_decorator


def init_points_on_rectangle(width, height, n=30):
    angles = np.linspace(0, 2 * np.pi, n)
    starting_points = np.transpose([np.sin(angles), np.cos(angles)])
    for i in range(0, len(starting_points)):
        starting_points[i] /= np.max(np.abs(starting_points[i]))
        starting_points[i, 0] *= width / 2
        starting_points[i, 1] *= height / 2
    return starting_points


def special_init_for_negative_spring():
    xs = np.concatenate((np.linspace(-5, -2.5, 10),
                         np.linspace(-2.5, -1.5, 20),
                         np.linspace(-2, 3, 10),
                         np.linspace(3, 5, 10)))
    ys = np.ones(len(xs)) * 5
    xs = np.concatenate((xs, -xs))
    ys = np.concatenate((ys, -ys))
    return np.array([xs, ys]).transpose()


def corner_case_dumping_init_points(width, height):
    outer = init_points_on_rectangle(width, height, 80)
    inner = np.array([np.linspace(-width / 2, width / 2, 31),
                      np.zeros(31)]).transpose()
    return np.concatenate((outer, inner))


def pythagoras(start, end):
    return np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)


def add_arrow(curve, arrows):
    arrows.append(1)
    prev, length = curve[0], 0
    for point in curve[1:]:
        length += pythagoras(point, prev)
        prev = point
    if length >= 2:
        prev, partial_length, i = curve[0], 0, 0
        for point in curve[1:]:
            partial_length += pythagoras(point, prev)
            if partial_length / length > arrows[i]:
                arrow_start_x = prev[0]
                arrow_start_y = prev[1]
                arrow_end_x = point[0]
                arrow_end_y = point[1]
                ax = plt.axes()
                ax.arrow(arrow_start_x, arrow_start_y,
                         (arrow_end_x - arrow_start_x) * 0.001,
                         (arrow_end_y - arrow_start_y) * 0.001,
                         head_width=0.2, head_length=0.2)
                i += 1
            prev = point


def for_name(name, width, height, arrows=None):
    if arrows is None:
        arrows = [0.2, 0.3]

    @plot(name + ".svg", width, height)
    def phase_portrait(diff_equation, get_starting_points):
        sp = get_starting_points()
        for initial_value in sp:
            solver = ode(diff_equation).set_integrator('zvode', method='bdf')
            solver.set_initial_value(initial_value, 0)
            dt, points = 0.01, [initial_value]

            while solver.successful() and solver.t < 100:
                point = solver.integrate(solver.t + dt)
                points.append(point)
                if np.abs(point[0]) > width / 2 or np.abs(point[1]) > height / 2:
                    break

            points = np.real(points)
            plt.plot(points[:, 0], points[:, 1], 'C0', linewidth=0.5)
            add_arrow(points, arrows)

    return phase_portrait


# for_name("van_der_poll_1", 10, 10, arrows=[0.2, 0.4]) \
#     (lambda t, y: van_der_poll(t, y, 1),
#      lambda: init_points_on_rectangle(10, 10))
# for_name("van_der_poll_5", 10, 10, arrows=[0.2, 0.4]) \
#     (lambda t, y: van_der_poll(t, y, 5),
#      lambda: init_points_on_rectangle(10, 10))
# for_name("van_der_poll_0", 10, 10, arrows=[0.1, 0.2]) \
#     (lambda t, y: van_der_poll(t, y, 0),
#      lambda: init_points_on_rectangle(10, 10))
# for_name("van_der_poll_0_5", 10, 10, arrows=[0.2, 0.5]) \
#     (lambda t, y: van_der_poll(t, y, 0.5),
#      lambda: init_points_on_rectangle(10, 10))
for_name("pendulum_1", 20, 10, arrows=[0.2, 0.6]) \
    (lambda t, y: pendulum(t, y, 1, 1),
     lambda: init_points_on_rectangle(20, 10, n=100))
for_name("pendulum_2", 20, 10, arrows=[0.2, 0.6]) \
    (lambda t, y: pendulum(t, y, 4, 1),
     lambda: init_points_on_rectangle(20, 10, n=100))
for_name("pendulum_3", 20, 10, arrows=[0.2, 0.6]) \
    (lambda t, y: pendulum(t, y, 4, 0),
     lambda: corner_case_dumping_init_points(20, 10))
for_name("pendulum_4", 20, 10, arrows=[0.2, 0.6]) \
    (lambda t, y: pendulum(t, y, 1, 3),
     lambda: corner_case_dumping_init_points(20, 10))
for_name("mechanical_1", 10, 10, arrows=[0.3, 0.6]) \
    (lambda t, y: mechanical_system(t, y, 1, 1, 1.5),
     lambda: init_points_on_rectangle(10, 10, n=50))
for_name("mechanical_2", 10, 10, arrows=[0.4, 0.6]) \
    (lambda t, y: mechanical_system(t, y, 1, 1, -1.5),
     lambda: special_init_for_negative_spring())

fileNames = []
for fileName in fileNames:
    call(['inkscape -D -z --file=tex/svg/' + fileName + '.svg' +
          ' --export-pdf=' + fileName + '.pdf --export-latex'], shell=True)
