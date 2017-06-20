import os
from itertools import tee

import mpl_toolkits.mplot3d as a3
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from subprocess import call

if not os.path.exists('./kary/tex/svg'):
    os.makedirs('./kary/tex/svg')


# first
def fun_1(i):
    return lambda x: x[0] ** 2 + x[1] ** 2 + 2 ** i * (x[1] - 1) ** 2


def double(iter):
    x, y = tee(iter)
    next(y)
    return zip(x, y)


pts_x = []
pts_y = []

for i in range(0, 10):
    x, y = minimize(fun_1(i), np.array([0, 0])).x
    pts_x.append(x)
    pts_y.append(y)

fig = plt.figure()

xs = np.linspace(-1, 1, 100)
ys = np.linspace(-0.5, 1.5, 100)
xs, ys = np.meshgrid(xs, ys)
zs = xs ** 2 + ys ** 2
plt.contour(xs, ys, zs, 20)
plt.plot([-2, 2], [1, 1], 'r', linewidth=2, label="Zbiór rozwiązań dopuszczalnych")
plt.plot(pts_x, pts_y, 'b*', label="Uzyskane punkty")
plt.plot([0], [1], 'ro', label="Rozwiązanie analityczne")
plt.plot([0], [0], 'bo', label="Minimum funkcji bez kary")
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.axis([-1, 1, -0.5, 1.5])
plt.legend(loc='lower right', prop={'size': 6})
plt.savefig("./kary/tex/svg/first_allowed.svg", bbox_inches='tight')
call(['inkscape -D -z --file=kary/tex/svg/first_allowed.svg' +
      ' --export-pdf=kary/tex/first_allowed.pdf --export-latex'], shell=True)

fig = plt.figure()
xs = [0] + pts_x
ys = [0] + pts_y
dist = []
for x, y in zip(xs, ys):
    dist.append(np.sqrt(np.array([x ** 2 + (y - 1) ** 2])))

plt.plot(dist)
plt.grid(True)
plt.ylabel("Odległość od wyniku analitycznego")
plt.xlabel("Numer iteracji")
plt.savefig("./kary/tex/svg/first_distance.svg", bbox_inches='tight')
call(['inkscape -D -z --file=kary/tex/svg/first_distance.svg' +
      ' --export-pdf=kary/tex/first_distance.pdf --export-latex'], shell=True)

fig = plt.figure()

ratio = []
for x, y in double(dist):
    ratio.append((1 - y) / (1 - x))

plt.plot(ratio)
plt.grid(True)
plt.ylabel("$\\frac{d_{i+1}}{d_i}$")
plt.xlabel("Numer iteracji")
plt.savefig("./kary/tex/svg/first_ratio.svg", bbox_inches='tight')
call(['inkscape -D -z --file=kary/tex/svg/first_ratio.svg' +
      ' --export-pdf=kary/tex/first_ratio.pdf --export-latex'], shell=True)


# second
def fun_2(i):
    return lambda x: np.sqrt(x[0] ** 2 + x[1] ** 2) + 2 ** i * ((x[0] + x[1] - 1) ** 2 + (x[0] + x[1] - 2) ** 2)


pts_x = []
pts_y = []

for i in range(0, 10):
    x, y = minimize(fun_2(i), np.array([0, 0])).x
    pts_x.append(x)
    pts_y.append(y)

fig = plt.figure()

xs = np.linspace(-0.5, 1.5, 100)
ys = np.linspace(-0.5, 1.5, 100)
xs, ys = np.meshgrid(xs, ys)
zs = np.sqrt(xs ** 2 + ys ** 2)
plt.contour(xs, ys, zs, 20)

x = np.linspace(-3, 3)
y = 1 - x
plt.plot(x, y, 'r', linewidth=2, label="Zbiór rozwiązań dopuszczalnych")
x = np.linspace(-3, 3)
y = 2 - x
plt.plot(x, y, 'r', linewidth=2)

plt.plot(pts_x, pts_y, 'b*', label="Uzyskane punkty")
plt.plot([0], [0], 'bo', label="Minimum funkcji bez kary")
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.axis([-0.5, 1.5, -0.5, 1.5])
plt.plot([-0.5, 1.5], [-0.5, 1.5], 'r--', linewidth=0.3, label="y = x")
plt.legend(loc='lower right', prop={'size': 6})
plt.savefig("./kary/tex/svg/second_scatter_points.svg", bbox_inches='tight')
call(['inkscape -D -z --file=kary/tex/svg/second_scatter_points.svg' +
      ' --export-pdf=kary/tex/second_scatter_points.pdf --export-latex'], shell=True)


def inner_penalty(k, c):
    x = np.array([3, 3])
    y = (x[0] + 1) ** 3 / 3 + x[1]
    it = 0
    xs = []
    while True:
        def penalized(x):
            res = (x[0] + 1) ** 3 / 3 + x[1]
            pen = k / (x[0] - 1) + k / (x[1])
            if x[0] < 1 or x[1] < 0:
                return 1000
            return res + pen

        res = minimize(penalized, x)
        xs.append(res.x)
        if np.abs(y - res.fun) < 0.01:
            return it, xs
        x, y = res.x, res.fun
        k /= c
        it += 1


ks = np.geomspace(2, 1000, 20)
cs = np.linspace(1.1, 2, 30)

k_s, c_s = np.meshgrid(ks, cs)
z_s = np.empty(c_s.shape)

for (i_k, k) in enumerate(ks):
    for (i_c, c) in enumerate(cs):
        z_s[i_c][i_k] = inner_penalty(k, c)[0]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.azim = 120
ax.set_xlabel("$K_0$")
ax.set_ylabel("c")
ax.set_zlabel("liczba iteracji")
p = ax.plot_surface(k_s, c_s, z_s, cmap="hot")
fig.colorbar(p, orientation="horizontal")
plt.savefig("./kary/tex/svg/third_iterations.svg", bbox_inches='tight')
call(['inkscape -D -z --file=kary/tex/svg/third_iterations.svg' +
      ' --export-pdf=kary/tex/third_iterations.pdf --export-latex'], shell=True)

fig = plt.figure()
xs = np.linspace(-0.5, 5, 100)
ys = np.linspace(-0.5, 10, 100)
x = np.linspace(1, 5, 100)
xs, ys = np.meshgrid(xs, ys)
zs = (xs + 1) ** 3 / 3 + ys

_, points = inner_penalty(100, 2)
points = np.array(points)
ax = fig.add_subplot(221)
ax.plot(points[:, 0], points[:, 1], 'C0*-', label="k=100, c=2")
ax.fill_between(x, np.zeros(x.size), np.ones(x.size) * 10, facecolor='yellow', alpha=0.3)
ax.contour(xs, ys, zs, 30)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.axhline(0, color='k')
ax.axvline(1, color='k')
ax.legend(loc='lower right', prop={'size': 6})

_, points = inner_penalty(20, 2)
points = np.array(points)
ax = fig.add_subplot(222)
ax.plot(points[:, 0], points[:, 1], 'C1*-', label="k=20, c=2")
ax.fill_between(x, np.zeros(x.size), np.ones(x.size) * 10, facecolor='yellow', alpha=0.3)
ax.contour(xs, ys, zs, 30)
ax.axhline(0, color='k')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.axvline(1, color='k')
ax.legend(loc='lower right', prop={'size': 6})

_, points = inner_penalty(100, 1.5)
points = np.array(points)
ax = fig.add_subplot(223)
ax.plot(points[:, 0], points[:, 1], 'C2*-', label="k=100, c=1.5")
ax.fill_between(x, np.zeros(x.size), np.ones(x.size) * 10, facecolor='yellow', alpha=0.3)
ax.contour(xs, ys, zs, 30)
ax.axhline(0, color='k')
ax.axvline(1, color='k')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.legend(loc='lower right', prop={'size': 6})

_, points = inner_penalty(20, 1.5)
points = np.array(points)
ax = fig.add_subplot(224)
ax.plot(points[:, 0], points[:, 1], 'C2*-', label="k=20, c=1.5")
ax.fill_between(x, np.zeros(x.size), np.ones(x.size) * 10, facecolor='yellow', alpha=0.3)
ax.contour(xs, ys, zs, 30)
ax.axhline(0, color='k')
ax.axvline(1, color='k')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.legend(loc='lower right', prop={'size': 6})

plt.savefig("./kary/tex/svg/third_optimization.svg", bbox_inches='tight')
call(['inkscape -D -z --file=kary/tex/svg/third_optimization.svg' +
      ' --export-pdf=kary/tex/third_optimization.pdf --export-latex'], shell=True)
