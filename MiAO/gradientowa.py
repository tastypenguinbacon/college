import os
from collections import namedtuple
from itertools import islice
from subprocess import call

import matplotlib.pyplot as plt

from algorithms.gradient import *
from algorithms.variable_metrics import DavidonFletcherPowell, WolfeBroydenDavidon, \
    BroydenFletcherGoldfarbShanno, Pearson1, Pearson2, McCromick

file_names = []
if not os.path.exists('gradienty/tex/svg'):
    os.makedirs('gradienty/tex/svg')

Solver = namedtuple('Solver', ['file_name', 'title', 'solver'])

gradient_methods = [
    Solver('fast_fall', 'Metoda najszyszego spadku', FastestDescending),
    Solver('fletcher_reeves', 'Metoda-Fletchera-Reevesa', FletcherReeves),
    Solver('polak_ribiere', 'Metoda-Polaka-Ribiere\'a', PolakRibiere),
    Solver('full_beta', 'Pełen wzór na współczynnik beta', FullBetaFormula)
]

variable_metrics = [
    Solver('davidon_fletcher_powell', 'Metoda Davidona-Fletchera-Powella', DavidonFletcherPowell),
    Solver('wolfe_broyden_davidon', 'Metoda Wolfe\'a-Broydena-Davidona', WolfeBroydenDavidon),
    Solver('broyedn_fletcher_goldfarb_shanno', 'Metoda Broydena-Fletchera-Godfarba-Shanno',
           BroydenFletcherGoldfarbShanno),
    Solver('pearson_1', 'Pierwsza metoda Pearsona', Pearson1),
    Solver('pearson_2', 'Druga metoda Pearsona', Pearson2),
    Solver('mccormick', 'Metoda McCormicka', McCromick)
]


def plot_background(min_x, max_x, min_y, max_y, fun):
    plot_size = np.average([max_x - min_x, max_y - min_y])

    delta = plot_size / 1000
    xs = np.arange(min_x, max_x, delta)
    ys = np.arange(min_y, max_y, delta)
    zs = np.array([[0] * len(xs)] * len(ys))
    for j, y in enumerate(iter(ys)):
        for i, x in enumerate(iter(xs)):
            zs[j, i] = fun(np.array([x, y]))

    return lambda: plt.contour(xs, ys, zs, 20, interpolation='gaussian')


def function_with_exponents(x):
    x1 = x[0]
    x2 = x[1]
    return (6 * x1 ** 2 + 6 * x1 * x2 + x2 ** 2
            + 4.5 * (np.exp(x1) - x1 - 1)
            + 1.5 * (np.exp(x2) - x2 - 1))


def gradient(function):
    d = 10e-9
    dx = np.array([d, 0])
    dy = np.array([0, d])

    def grad(x):
        up = (function(x + dx) - function(x)) / d
        down = (function(x + dy) - function(x)) / d
        return np.array([up, down])

    return grad


def quadratic_form():
    for a in [1, 0.5, 0.3]:
        def quadratic_form(x):
            A = np.array([[1, 0], [0, a]])
            return x @ A @ x

        yield quadratic_form, a


def decorate_plot(data, limits, background, title):
    plt.figure()

    plt.plot(data[:, 0], data[:, 1], 'r+')
    plt.plot(data[:, 0], data[:, 1], 'b-')

    plt.axis(limits)
    plt.title('')
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.grid(True)
    background()


# pierwsze
min_x, max_x, min_y, max_y = -2.5, 10.5, -2.5, 10.5
for fun, a in quadratic_form():
    solver = FastestDescending(fun, gradient(fun))
    x0 = np.array([10, 10])
    solved_points = np.array(list(solver.trim(solver(x0))))
    file_name = ('first_%f' % a).replace('.', '_')
    background = plot_background(min_x, max_x, min_y, max_y, fun)
    title = ''
    decorate_plot(solved_points, [min_x, max_x, min_y, max_y], background, '')
    plt.savefig('gradienty/tex/svg/' + file_name + '.svg', bbox_inches='tight')
    file_names.append(file_name)
    plt.close()


def statistics(data, file_name, min_point, min_val):
    xs, ys = data[:, 0], data[:, 1]
    value_diff, diff = [], []
    for x, y in zip(xs, ys):
        value_diff.append(function_with_exponents(np.array([x, y])) - min_val)
    for x, y in zip(xs, ys):
        diff.append(np.linalg.norm(np.array(x, y) - min_point))
    plt.plot(value_diff)
    plt.xlabel('numer iteracji')
    plt.ylabel('różnica wartości')
    plt.grid(True)
    plt.savefig(file_name + '_values.svg', bbox_inches='tight')
    file_names.append(file_name.split('/')[-1] + '_values')
    plt.close()
    plt.plot(diff)
    plt.xlabel('numer iteracji')
    plt.ylabel('odległość od minimum')
    plt.grid(True)
    plt.savefig(file_name + '_distance.svg', bbox_inches='tight')
    file_names.append(file_name.split('/')[-1] + '_distance')
    plt.close()
    plt.figure()
    plt.xlabel('numer iteracji')
    plt.ylabel('norma z gradientu')
    grad = gradient(function_with_exponents)
    gradient_norms = []
    for x, y in zip(xs, ys):
        gradient_norms.append(np.linalg.norm(grad(np.array([x, y]))))
    plt.grid(True)
    plt.plot(gradient_norms)
    plt.savefig(file_name + '_grad_norm.svg', bbox_inches='tight')
    file_names.append(file_name.split('/')[-1] + '_grad_norm')
    plt.close()

# drugie
min_x, max_x, min_y, max_y = -3, 3, -3, 3
background = plot_background(min_x, max_x, min_y, max_y, function_with_exponents)

for file_name, title, solver_class in gradient_methods:
    solver = solver_class(function_with_exponents, gradient(function_with_exponents))
    x0 = np.array([-3, 3])
    solved_points = np.array(list(islice(solver(x0), 0, 20)))
    decorate_plot(solved_points, [min_x, max_x, min_y, max_y], background, '')
    full_file_name = 'gradienty/tex/svg/second_' + file_name
    file_names.append('second_' + file_name)
    plt.savefig(full_file_name + '.svg', bbox_inches='tight')
    plt.close()
    statistics(solved_points, full_file_name, np.array([0, 0]), function_with_exponents(np.array([0, 0])))
else:
    solver = FastestDescending(function_with_exponents, gradient(function_with_exponents))
    x0 = np.array([-3, 1])
    solved_points = np.array(list(islice(solver(x0), 0, 20)))
    title = ''
    file_name = 'fast_fall_2'
    decorate_plot(solved_points, [min_x, max_x, min_y, max_y], background, '')
    full_file_name = 'gradienty/tex/svg/second_' + file_name + '_2'
    file_names.append('second_' + file_name + '_2')
    plt.savefig(full_file_name + '.svg', bbox_inches='tight')
    plt.close()
    statistics(solved_points, full_file_name, np.array([0, 0]), function_with_exponents(np.array([0, 0])))

# trzecie
min_x, max_x, min_y, max_y = -2.5, 10.5, -2.5, 10.5
for file_name, title, solver_class in variable_metrics:
    for fun, a in quadratic_form():
        solver = solver_class(fun, gradient(fun))
        x0 = np.array([10, 10])
        solved_points = np.array(list(solver.trim(solver(x0))))
        file_name = ('third' + file_name + '_%f' % a).replace('.', '_')
        background = plot_background(min_x, max_x, min_y, max_y, fun)
        decorate_plot(solved_points, [min_x, max_x, min_y, max_y], background, '')
        plt.savefig('gradienty/tex/svg/' + file_name + '.svg', bbox_inches='tight')
        file_names.append(file_name)
        plt.close()

# czwarte
min_x, max_x, min_y, max_y = -3, 3, -3, 3
background = plot_background(min_x, max_x, min_y, max_y, function_with_exponents)

for file_name, title, solver_class in variable_metrics:
    solver = solver_class(function_with_exponents, gradient(function_with_exponents))
    x0 = np.array([-3, 3])
    solved_points = np.array(list(solver.trim((solver(x0)))))
    decorate_plot(solved_points, [min_x, max_x, min_y, max_y], background, '')
    full_file_name = 'gradienty/tex/svg/fourth_' + file_name
    file_names.append('fourth_' + file_name)
    plt.savefig(full_file_name + '.svg', bbox_inches='tight')
    plt.close()
    statistics(solved_points, full_file_name, np.array([0, 0]), function_with_exponents(np.array([0, 0])))

tex_image_format = '''
\\begin{figure}[H]
    \\centering
    \\def \\svgwidth{0.7\\columnwidth}
    \\input{%s.pdf_tex}
    \\caption{TODO}
\\end{figure}\\noindent
'''

with open('gradienty/tex/temp.tex', mode='w') as temp_tex:
    for fileName in file_names:
        call(['inkscape -D -z --file=gradienty/tex/svg/' + fileName + '.svg' +
              ' --export-pdf=gradienty/tex/' + fileName + '.pdf --export-latex'], shell=True)
        print(tex_image_format % fileName, file=temp_tex)
