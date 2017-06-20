import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3
from scipy.optimize import linprog
import numpy as np
from matplotlib import colors
import os
from subprocess import call

if not os.path.exists('./linear_programming/tex/svg'):
    os.makedirs('./linear_programming/tex/svg')


def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value - minimum) / (maximum - minimum)
    b = int(max(0, 255 * (1 - ratio)))
    r = int(max(0, 255 * (ratio - 1)))
    g = 255 - b - r
    if r < 0 or g < 0 or b < 0:
        return "#00000000"
    return '#%02X%02X%02X%02X' % (r, g, b, 255)

to_rgb = np.vectorize(lambda x: rgb(0, 1500000, x))

# 0.3 x + 0.5 y + 0.4 z <= 1800
# 0.1 x + 0.08 y + 0.12 z <= 500
# 0.06 x + 0.04 y + 0.05 z <= 200
# -x <= 0
# -y <= 0
# -z <= 0
# max 400 x + 300 y + 200 z
#
A = np.array([
    [0.3, 0.5, 0.4],
    [0.1, 0.08, 0.12],
    [0.06, 0.04, 0.05]
])

b = np.array([1800, 500, 200])

fun = np.array([400, 300, 200])

print(linprog(-fun, A, b))

xs = np.linspace(0, 3600, 361)
ys = np.linspace(0, 3600, 361)
xs, ys = np.meshgrid(xs, ys)
zs = np.min([
    ((1800 - 0.30 * xs - 0.50 * ys) / 0.40),
    ((500 - 0.10 * xs - 0.08 * ys) / 0.12),
    ((200 - 0.06 * xs - 0.04 * ys) / 0.05)
], axis=0)

zs[zs < 0] = np.NaN

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.azim = 20
ax.set_xlim(0, 3500)
ax.set_ylim(0, 3500)
ax.set_zlim(0, 4500)

colors = np.array(400 * xs + 300 * ys + 200 * zs)
ax.plot([1555.55555556], [2666.66666667], [0.], 'bo')
colors[np.isnan(colors)] = 0
colors = to_rgb(colors)

plt.cm.jet.set_bad(alpha=0.0)
plot = ax.plot_surface(xs, ys, zs, rcount=200, ccount=200, facecolors=colors, linewidth=0)
ax.set_xlabel("$x_A$")
ax.set_ylabel("$x_B$")
ax.set_zlabel("$x_C$")
plt.savefig("./linear_programming/tex/svg/first.svg", bbox_inches='tight')
call(['inkscape -D -z --file=linear_programming/tex/svg/first.svg' +
      ' --export-pdf=linear_programming/tex/first.pdf --export-latex'], shell=True)

xs = np.linspace(0, 3600, 361)
ys = np.linspace(0, 3600, 361)
xs, ys = np.meshgrid(xs, ys)
zs2 = xs * 400 + ys * 300
print(zs2 < 0)
zs2 = to_rgb(zs2)

zs3 = xs * 400 + ys * 300
zs3[np.isnan(zs)] = np.nan
fig = plt.figure()
cax = plt.contourf(xs, ys, zs3, 100)
plt.plot([1555.55555556], [2666.66666667], 'bo')
plt.xlabel("$x_A$")
plt.ylabel("$x_B$")
plt.grid(True)
cbar = fig.colorbar(cax)


plt.savefig("./linear_programming/tex/svg/bottom.svg")
call(['inkscape -D -z --file=linear_programming/tex/svg/bottom.svg' +
      ' --export-pdf=linear_programming/tex/bottom.pdf --export-latex'], shell=True)


A = np.array([
    [1, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, -1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, -1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, -1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, -1],
    [1, 0, -1, -1, 0],
    [-1, 0, 1, 1, 0],
    [0, 1, 1, 0, -1],
    [0, -1, -1, 0, 1]
])

b = np.array([
    5,
    -3,
    3,
    -1,
    3,
    -1,
    3,
    -1,
    4,
    -4,
    0,
    0,
    0,
    0
])

c = np.array([6, 10, 4, 7, 3])

print(linprog(c, A, b))
plt.figure()

plt.plot(
      [1, 1, 2, 3, 3, 2, 1],
      [2, 3, 3, 2, 1, 1, 2]
)
plt.grid()
plt.xlabel("$I_3$")
plt.ylabel("$I_4$")
plt.savefig("./linear_programming/tex/svg/hexagon.svg", bbox_inches='tight')
call(['inkscape -D -z --file=linear_programming/tex/svg/hexagon.svg' +
      ' --export-pdf=linear_programming/tex/hexagon.pdf --export-latex'], shell=True)

