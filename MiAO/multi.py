import os
import mpl_toolkits.mplot3d as a3
from control import tf
from control import step
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from subprocess import call

if not os.path.exists('./multi/tex/svg'):
    os.makedirs('./multi/tex/svg')

lower_bound, upper_bound = 3, 5

r_i = np.linspace(lower_bound, upper_bound, 100)
r_a = np.linspace(0, 30, 100)

r_i, r_a = np.meshgrid(r_i, r_a)
power = r_a / (r_i + r_a) ** 2

fig = plt.figure()
plt.grid(True)
plt.xlabel('$R_i$')
plt.ylabel('$R_a$')
plot = plt.contourf(r_i, r_a, power, 300)
fig.colorbar(plot)

plt.savefig("./multi/tex/svg/power.svg", bbox_inches='tight')
call(['inkscape -D -z --file=multi/tex/svg/power.svg' +
      ' --export-pdf=multi/tex/power.pdf --export-latex &'], shell=True)

efficiency = r_a / (r_i + r_a)

fig = plt.figure()
plt.grid(True)
plt.xlabel('$R_i$')
plt.ylabel('$R_a$')
plot = plt.contourf(r_i, r_a, efficiency, 300)
fig.colorbar(plot)

plt.savefig("./multi/tex/svg/efficiency.svg", bbox_inches='tight')
call(['inkscape -D -z --file=multi/tex/svg/efficiency.svg' +
      ' --export-pdf=multi/tex/efficiency.pdf --export-latex &'], shell=True)

K = np.linspace(-0.99, 5, 100)
x = np.linspace(1, 5, 100)
K, x = np.meshgrid(K, x)

overshoot = np.exp(-(x / (K + 1) * np.pi) / (np.sqrt(1 - (x / (K + 1)) ** 2)))
overshoot[np.logical_or(np.imag(overshoot) != 0, np.isnan(overshoot))] = 0
fig = plt.figure()

plot = plt.contourf(K, x, overshoot, 300)
plt.plot([-0.99, 10], [0.01, 11], 'white', label='Powyżej brak oscylacji')
plt.grid(True)
plt.xlabel('K')
plt.ylabel('x')
plt.xlim([-0.99, 5])
plt.ylim([1, 5])
fig.colorbar(plot)

plt.savefig("./multi/tex/svg/overshoot.svg", bbox_inches='tight')
call(['inkscape -D -z --file=multi/tex/svg/overshoot.svg' +
      ' --export-pdf=multi/tex/overshoot.pdf --export-latex &'], shell=True)

static_diff = 1 / (1 + K)

fig = plt.figure()
plt.grid(True)
plt.xlabel('$K$')
plt.ylabel('Uchyb statyczny')
plt.xlim([-0.99, 5])
K = np.linspace(-0.99, 5, 100)
OP = 1 / (1 + K)
ax = plt.semilogy(K, OP)

plt.savefig("./multi/tex/svg/static2d.svg", bbox_inches='tight')
call(['inkscape -D -z --file=multi/tex/svg/static2d.svg' +
      ' --export-pdf=multi/tex/static2d.pdf --export-latex &'], shell=True)

plt.show()
