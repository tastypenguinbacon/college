import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import ode

from diff_equations import get_jacobian_for_point, linear_form


def pythagoras(start, end):
    return np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)


def add_arrow(curve, arrows, color, relative_size=10):
    arrows.append(1)
    prev, length = curve[0], 0
    for point in curve[1:]:
        length += pythagoras(point, prev)
        prev = point
    if length != 0:
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
                         head_width=0.2 * relative_size / 10,
                         head_length=0.2 * relative_size / 10, color=color)
                i += 1
            prev = point


fileNames = []


def for_name(name, width, height, arrows=None, linear=0):
    if arrows is None:
        arrows = [0.2, 0.3]

    fileNames.append(name)

    @plot(name + ".svg", width, height)
    def phase_portrait(diff_equation, get_starting_points, fillings=None):
        if fillings is None:
            fillings = []
        sp = get_starting_points()
        colors_and_functions = [('C0', diff_equation)]
        jacobian = get_jacobian_for_point(np.array([0, 0]), diff_equation)
        if linear == 1:
            colors_and_functions = [('C2', lambda t, y: linear_form(y, jacobian))]
        if linear == 2:
            colors_and_functions.append(('C2', lambda t, y: linear_form(y, jacobian)))

        for color, function in colors_and_functions:
            for initial_value in sp:
                solver = ode(function).set_integrator('zvode', method='bdf')
                solver.set_initial_value(initial_value, 0)
                dt, points = 0.01, [initial_value]

                while solver.successful() and solver.t < 100:
                    point = solver.integrate(solver.t + dt)
                    points.append(point)
                    if np.abs(point[0]) > width / 2 or np.abs(point[1]) > height / 2:
                        break

                points = np.real(points)
                plt.plot(points[:, 0], points[:, 1], color, linewidth=0.5)
                add_arrow(points, arrows, relative_size=np.sqrt(width * height), color=color)
        for filling in fillings:
            filling()

    return phase_portrait


def plot(file_name, width, height):
    def plot_decorator(f):
        def wrapped(function_name, init_point_provider, fillings=None):
            if fillings is None:
                fillings = []
            fig = plt.figure()
            f(function_name, init_point_provider, fillings)
            plt.axis([-width / 2, width / 2, -height / 2, height / 2])
            plt.xlabel("x1")
            plt.ylabel("x2")
            plt.savefig('tex/svg/' + file_name, bbox_inches='tight')
            fig.canvas.mpl_connect('button_press_event',
                                   lambda event: print("x=%f, y=%f" % (event.xdata, event.ydata)))

        return wrapped

    return plot_decorator
