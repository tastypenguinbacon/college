import os
import mpl_toolkits.mplot3d as a3
from control import tf
from control import step
import numpy as np
import matplotlib.pyplot as plt
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
fig = plt.figure()
plt.ylabel('$\mu$')
plt.xlabel('$\eta$')
plt.xlim([0, 1])
plt.ylim([0, 0.1])
plt.grid(True)
R_i = np.linspace(3, 5, 5)
for i in R_i:
    eta = np.linspace(0, 1, 100)
    mu = eta * (1 - eta) / i
    plt.plot(eta, mu, label='$R_i=%0.2f$' % i)

eta = np.linspace(0.5, 1, 100)
mu = eta * (1 - eta) / 3
plt.plot(eta, mu, 'r', linewidth=5, label="Zbiór rozwiązań kompromisowych")
plt.legend(loc='lower right', prop={'size': 6})
plt.savefig("./multi/tex/svg/contour_overlay.svg", bbox_inches='tight')
call(['inkscape -D -z --file=multi/tex/svg/contour_overlay.svg' +
      ' --export-pdf=multi/tex/contour_overlay.pdf --export-latex &'], shell=True)

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

fig = plt.figure()
x = np.geomspace(1, 10 ** 2, 5)
shts = np.linspace(0.0001, 0.99, 1000)
for i in x:
    z = np.exp(-np.pi / np.sqrt(1 / (i * shts) ** 2 - 1))
    z[np.isnan(z)] = 0
    plt.plot(shts, z, label='x=%d' % i)
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.grid(True)
plt.scatter([0], [1], s=[100], label='zbiór kompromisów - punkt (0,1)', c='red')
plt.legend(loc='lower right', prop={'size': 6})
plt.savefig("./multi/tex/svg/overshoot_static_overlay.svg", bbox_inches='tight')
call(['inkscape -D -z --file=multi/tex/svg/overshoot_static_overlay.svg' +
      ' --export-pdf=multi/tex/overshoot_static_overlay.pdf --export-latex &'], shell=True)
fig = plt.figure()
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y')
plt.xlim([0, 100])
for T in np.linspace(100, 500, 5):
    G = tf([10], [T, T + 1, 10 + 1])
    y, x = step(G, T=np.linspace(0, 100, 300))
    plt.plot(x, y, label="$K=%d, T=%d, T_o=1$" % (10, T))

plt.legend(loc='lower right', prop={'size': 6})
plt.savefig("./multi/tex/svg/badumpts.svg", bbox_inches='tight')
call(['inkscape -D -z --file=multi/tex/svg/badumpts.svg' +
      ' --export-pdf=multi/tex/badumpts.pdf --export-latex &'], shell=True)
n = np.arange(1, 8, 1)
Q1 = np.array([40, 60, 60, 10, 20, 30, 40])
Q2 = np.array([10, 30, 20, 30, 5, 20, 25])
Q3 = 100 - Q2

fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 100, 10)
ax.fill_between(x, 0, 100 - x, alpha=0.3, color='green', label='Zbiór dopuszczalny')
plt.grid(True)
plt.xlabel('$Q_1[\%]$')
plt.ylabel('$Q_1[\%]$')
plt.xlim([0, np.max(Q1) + 10])
plt.ylim([0, np.max(Q2) + 10])
plt.scatter(Q1, Q2)

for i, x, y in zip(n, Q1, Q2):
    plt.annotate(i, xy=(x, y), xytext=(-5, 5), textcoords='offset points', ha='right', va='bottom')

plt.legend(loc='lower right', prop={'size': 6})
plt.savefig("./multi/tex/svg/scatter.svg", bbox_inches='tight')
call(['inkscape -D -z --file=multi/tex/svg/scatter.svg' +
      ' --export-pdf=multi/tex/scatter.pdf --export-latex &'], shell=True)

fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 100, 10)
ax.fill_between(x, x, 100, alpha=0.3, color='green', label='Zbiór dopuszczalny')
plt.grid(True)
plt.xlabel('$Q_1[\%]$')
plt.ylabel('$Q_3[\%]$')
plt.xlim([0, np.max(Q1) + 10])
plt.ylim([0, 100])
plt.scatter(Q1, Q3)

for i, x, y in zip(n, Q1, Q3):
    plt.annotate(i, xy=(x, y), xytext=(-5, 5), textcoords='offset points', ha='right', va='bottom')

plt.legend(loc='lower right', prop={'size': 6})
plt.savefig("./multi/tex/svg/only_working.svg", bbox_inches='tight')
call(['inkscape -D -z --file=multi/tex/svg/only_working.svg' +
      ' --export-pdf=multi/tex/only_working.pdf --export-latex &'], shell=True)

fig = plt.figure()
plt.grid(True)
plt.bar(n - 0.2, Q1, width=0.2, label='$Q1$')
plt.bar(n + 0.0, Q2, width=0.2, label='$Q2$')
plt.bar(n + 0.2, Q3, width=0.2, label='$Q3$')
plt.xlabel('Numer próbki')
plt.ylabel('$Q_i[\%]$')
plt.legend(loc='lower right', prop={'size': 6})
plt.savefig("./multi/tex/svg/together.svg", bbox_inches='tight')
call(['inkscape -D -z --file=multi/tex/svg/together.svg' +
      ' --export-pdf=multi/tex/together.pdf --export-latex &'], shell=True)

plt.show()
