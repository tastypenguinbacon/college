import os
from subprocess import call
from time import time

import matplotlib.pyplot as plt

from diff_equations import *
from initial_conditions import special_init_for_negative_spring, init_points_on_rectangle, \
    corner_case_dumping_init_points
from plot import fileNames, for_name

if not os.path.exists('tex/svg'):
    os.makedirs('tex/svg')

begin = time()

width, height = 10, 10
for_name("van_der_poll_1", width, height, arrows=[0.2, 0.6]) \
    (lambda t, y: van_der_poll(y, 1),
     lambda: init_points_on_rectangle(width, height), [
         lambda: plt.plot([0], [0], 'ro', label="Punkt stabilny")
     ])

for_name("van_der_poll_1_lin", width, height, arrows=[0.2, 0.6], linear=1) \
    (lambda t, y: van_der_poll(y, 1),
     lambda: init_points_on_rectangle(width, height, n=40), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])

for_name("van_der_poll_1_both_far", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: van_der_poll(y, 1),
     lambda: init_points_on_rectangle(width, height, n=40), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])

width /= 10
height /= 10
for_name("van_der_poll_1_both_close", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: van_der_poll(y, 1),
     lambda: init_points_on_rectangle(width, height, n=20), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])

width, height = 10, 10
for_name("van_der_poll_5", width, height, arrows=[0.2, 0.6]) \
    (lambda t, y: van_der_poll(y, 5),
     lambda: init_points_on_rectangle(width, height), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])

for_name("van_der_poll_5_lin", width, height, arrows=[0.2, 0.6], linear=1) \
    (lambda t, y: van_der_poll(y, 5),
     lambda: init_points_on_rectangle(width, height, n=40), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])

for_name("van_der_poll_5_both_far", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: van_der_poll(y, 5),
     lambda: init_points_on_rectangle(width, height, n=40), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])

width /= 10
height /= 10
for_name("van_der_poll_5_both_close", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: van_der_poll(y, 5),
     lambda: init_points_on_rectangle(width, height, n=20), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])

width, height = 10, 10
for_name("van_der_poll_0", width, height, arrows=[0.1, 0.2]) \
    (lambda t, y: van_der_poll(y, 0),
     lambda: init_points_on_rectangle(width, height))

for_name("van_der_poll_0_lin", width, height, arrows=[0.2, 0.6], linear=1) \
    (lambda t, y: van_der_poll(y, 0),
     lambda: init_points_on_rectangle(width, height, n=40))

for_name("van_der_poll_0_both_far", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: van_der_poll(y, 0),
     lambda: init_points_on_rectangle(width, height, n=40))

width /= 10
height /= 10
for_name("van_der_poll_0_both_close", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: van_der_poll(y, 0),
     lambda: init_points_on_rectangle(width, height, n=20))

width, height = 10, 10
for_name("van_der_poll_0_5", width, height, arrows=[0.2, 0.6]) \
    (lambda t, y: van_der_poll(y, 0.5),
     lambda: init_points_on_rectangle(width, height), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])
for_name("van_der_poll_0_5_lin", width, height, arrows=[0.2, 0.6], linear=1) \
    (lambda t, y: van_der_poll(y, 0.5),
     lambda: init_points_on_rectangle(width, height, n=40), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])

for_name("van_der_poll_0_5_both_far", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: van_der_poll(y, 0.5),
     lambda: init_points_on_rectangle(width, height, n=40), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])

width /= 10
height /= 10
for_name("van_der_poll_0_5_both_close", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: van_der_poll(y, 0.5),
     lambda: init_points_on_rectangle(width, height, n=20), [
        lambda: plt.plot([0],[0], 'ro', label="Punkt stabilny")
     ])

temp = lambda x: 0.02517517 * x ** 3 + 0.23480313 * x ** 2 - 0.93830795 * x - 4.47556726 if -8 < x < 1 else -255 * x - 6
x = np.linspace(-20, 20, 300)
right = lambda x: temp(x - 2 * np.pi)
more_right = lambda x: right(x - 2 * np.pi)
middle = lambda x: right(x + 2 * np.pi)
left = lambda x: middle(x + 2 * np.pi)
left = np.array(list(map(left, x)))
middle = np.array(list(map(middle, x)))
more_right = np.array(list(map(more_right, x)))
right = np.array(list(map(right, x)))
height, width = 10, 20

for_name("pendulum_1", 20, 10, arrows=[0.2, 0.6]) \
    (lambda t, y: pendulum(y, 1, 1),
     lambda: init_points_on_rectangle(20, 10, n=100),
     [lambda: plt.fill_between(x, left, -height / 2 * np.ones(len(x)),
                               where=left > -height / 2,
                               facecolor='red', alpha=0.1),
      lambda: plt.fill_between(x, more_right, height / 2 * np.ones(len(x)),
                               where=right < height / 2,
                               facecolor='orange', alpha=0.1),
      lambda: plt.fill_between(x, more_right, right,
                               where=right < more_right / 2,
                               facecolor='green', alpha=0.1),
      lambda: plt.fill_between(x, left, middle,
                               where=left < middle,
                               facecolor='blue', alpha=0.1),
      lambda: plt.fill_between(x, middle, right,
                               where=left < right,
                               facecolor='yellow', alpha=0.1)
      ])

for_name("pendulum_1_lin", width, height, arrows=[0.2, 0.6], linear=1) \
    (lambda t, y: pendulum(y, 1, 1),
     lambda: init_points_on_rectangle(width, height, n=100))

for_name("pendulum_1_both_far", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: pendulum(y, 1, 1),
     lambda: init_points_on_rectangle(width, height, n=100))

width /= 10
height /= 10
for_name("pendulum_1_both_close", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: pendulum(y, 1, 1),
     lambda: init_points_on_rectangle(width, height, n=20))

temp = lambda x: -2.267609 * x - 6.77998446
x = np.linspace(-20, 20, 300)
right = lambda x: temp(x - 2 * np.pi)
more_right = lambda x: right(x - 2 * np.pi)
middle = lambda x: right(x + 2 * np.pi)
left = lambda x: middle(x + 2 * np.pi)
left = np.array(list(map(left, x)))
middle = np.array(list(map(middle, x)))
more_right = np.array(list(map(more_right, x)))
right = np.array(list(map(right, x)))
height, width = 10, 20

for_name("pendulum_2", width, height, arrows=[0.2, 0.6]) \
    (lambda t, y: pendulum(y, 4, 1),
     lambda: init_points_on_rectangle(20, 10, n=100),
     [lambda: plt.fill_between(x, left, -height / 2 * np.ones(len(x)),
                               where=left > -height / 2,
                               facecolor='red', alpha=0.1),
      lambda: plt.fill_between(x, more_right, height / 2 * np.ones(len(x)),
                               where=right < height / 2,
                               facecolor='orange', alpha=0.1),
      lambda: plt.fill_between(x, more_right, right,
                               where=right < more_right / 2,
                               facecolor='green', alpha=0.1),
      lambda: plt.fill_between(x, left, middle,
                               where=left < middle,
                               facecolor='blue', alpha=0.1),
      lambda: plt.fill_between(x, middle, right,
                               where=left < right,
                               facecolor='yellow', alpha=0.1)
      ])

for_name("pendulum_2_lin", width, height, arrows=[0.2, 0.6], linear=1) \
    (lambda t, y: pendulum(y, 4, 1),
     lambda: init_points_on_rectangle(width, height, n=100))

for_name("pendulum_2_both_far", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: pendulum(y, 4, 1),
     lambda: init_points_on_rectangle(width, height, n=100))

width /= 10
height /= 10
for_name("pendulum_2_both_close", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: pendulum(y, 4, 1),
     lambda: init_points_on_rectangle(width, height, n=20))

for_name("pendulum_3", 20, 10, arrows=[0.2, 0.6]) \
    (lambda t, y: pendulum(y, 4, 0),
     lambda: corner_case_dumping_init_points(20, 10))

x = np.linspace(-20, 20, 300)
right = lambda x: -3.26072184 * x + 10.24415909
more_right = lambda x: right(x - 2 * np.pi)
middle = lambda x: right(x + 2 * np.pi)
left = lambda x: middle(x + 2 * np.pi)
left = np.array(list(map(left, x)))
middle = np.array(list(map(middle, x)))
more_right = np.array(list(map(more_right, x)))
right = np.array(list(map(right, x)))
height, width = 10, 20

for_name("pendulum_4", width, height, arrows=[0.2, 0.6]) \
    (lambda t, y: pendulum(y, 1, 3),
     lambda: init_points_on_rectangle(width, height, 80),
     [lambda: plt.fill_between(x, left, -height / 2 * np.ones(len(x)),
                               where=left > -height / 2,
                               facecolor='red', alpha=0.1),
      lambda: plt.fill_between(x, more_right, height / 2 * np.ones(len(x)),
                               where=right < height / 2,
                               facecolor='orange', alpha=0.1),
      lambda: plt.fill_between(x, more_right, right,
                               where=right < more_right / 2,
                               facecolor='green', alpha=0.1),
      lambda: plt.fill_between(x, left, middle,
                               where=left < middle,
                               facecolor='blue', alpha=0.1),
      lambda: plt.fill_between(x, middle, right,
                               where=left < right,
                               facecolor='yellow', alpha=0.1)
      ])

for_name("pendulum_4_lin", width, height, arrows=[0.2, 0.6], linear=1) \
    (lambda t, y: pendulum(y, 1, 3),
     lambda: init_points_on_rectangle(width, height, 80))

for_name("pendulum_4_both_far", width, height, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: pendulum(y, 1, 3),
     lambda: init_points_on_rectangle(20, 10, 80))

for_name("pendulum_4_both_close", 2, 1, arrows=[0.2, 0.6], linear=2) \
    (lambda t, y: pendulum(y, 1, 3),
     lambda: init_points_on_rectangle(2, 1, 20))

for_name("mechanical_1", 10, 10, arrows=[0.3, 0.6]) \
    (lambda t, y: mechanical_system(y, 1, 1, 1.5),
     lambda: init_points_on_rectangle(10, 10, n=30))

for_name("mechanical_1_lin", 10, 10, arrows=[0.3, 0.6], linear=1) \
    (lambda t, y: mechanical_system(y, 1, 1, 1.5),
     lambda: init_points_on_rectangle(10, 10, n=30))

for_name("mechanical_1_both_far", 10, 10, arrows=[0.3, 0.6], linear=2) \
    (lambda t, y: mechanical_system(y, 1, 1, 1.5),
     lambda: init_points_on_rectangle(10, 10, n=30))

for_name("mechanical_1_both_close", 1, 1, arrows=[0.3, 0.6], linear=2) \
    (lambda t, y: mechanical_system(y, 1, 1, 1.5),
     lambda: init_points_on_rectangle(1, 1, n=20))

width, height = 4, 4
x = np.linspace(-width / 2, width / 2)
lower_poly = lambda x: -0.13094286 * x ** 3 + 0.37710916 * x ** 2 - 1.08021611 * x - 1.1802789
upper_poly = lambda x: -lower_poly(-x)
upper_poly = np.array(list(map(upper_poly, x)))
lower_poly = np.array(list(map(lower_poly, x)))

for_name("mechanical_2", width, height, arrows=[0.4, 0.6]) \
    (lambda t, y: mechanical_system(y, 1, 1, -1.5),
     lambda: special_init_for_negative_spring(),
     [lambda: plt.fill_between(x, lower_poly, -height / 2 * np.ones(len(x)),
                               where=lower_poly > -height / 2,
                               facecolor='red', alpha=0.1),
      lambda: plt.fill_between(x, upper_poly, height / 2 * np.ones(len(x)),
                               where=upper_poly < height / 2,
                               facecolor='red', alpha=0.1),
      lambda: plt.fill_between(x, lower_poly, upper_poly,
                               where=lower_poly < upper_poly,
                               facecolor='green', alpha=0.1)
      ])

for_name("mechanical_2_lin", width, height, arrows=[0.4, 0.6], linear=1) \
    (lambda t, y: mechanical_system(y, 1, 1, -1.5),
     lambda: init_points_on_rectangle(width, height))

for_name("mechanical_2_both_far", width, height, arrows=[0.4, 0.6], linear=2) \
    (lambda t, y: mechanical_system(y, 1, 1, -1.5),
     lambda: special_init_for_negative_spring())

for_name("mechanical_2_both_close", width / 10, height / 10, arrows=[0.4, 0.6], linear=2) \
    (lambda t, y: mechanical_system(y, 1, 1, -1.5),
     lambda: init_points_on_rectangle(width / 10, height / 10, n=20))

tex_image_format = """
\\begin{figure}[H]
    \\centering
    \\def \\svgwidth{0.7\\columnwidth}
    \\input{%s.pdf_tex}
    \\caption{TODO}
\\end{figure}\\noindent
"""
with open('tex/temp.tex', mode='w') as temp_tex:
    for fileName in fileNames:
        call(['inkscape -D -z --file=tex/svg/' + fileName + '.svg' +
              ' --export-pdf=tex/' + fileName + '.pdf --export-latex'], shell=True)
        print(tex_image_format % fileName, file=temp_tex)

end = time()
print(end - begin)
