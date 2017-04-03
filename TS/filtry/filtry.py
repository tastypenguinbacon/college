import os
from control import tf
from control import bode
from subprocess import call
import numpy as np

import matplotlib.pyplot as plt

if not os.path.exists('svg'):
    os.makedirs('svg')


def plot(file_name):
    def plot_decorator(f):
        def wrapped():
            plt.figure()
            f()
            plt.legend(loc='lower right', prop={'size': 6})
            plt.savefig(file_name, bbox_inches='tight')

        wrapped()
        return wrapped

    return plot_decorator


@plot('svg/P.svg')
def p_regulator():
    for k in np.geomspace(1, 10 ** 3, 4, True):
        P = tf([k], [1])
        bode(P, dB=True, Plot=True, label='k = ' + str(k))


@plot('svg/PD.svg')
def pd_regulator():
    k = 1
    omega = np.geomspace(10 ** -1, 10 ** 5, 1000, True)
    for T_d in np.geomspace(1, 10 ** -3, 4, True):
        PD = k * tf([T_d, 1], 10)
        bode(PD, omega=omega, dB=True, Plot=True, label='k = 1, T_d = ' + str(T_d))


@plot('svg/PI.svg')
def pi_regulator():
    k = 1
    omega = np.geomspace(10 ** -1, 10 ** 5, 1000, True)
    for T_i in np.geomspace(1, 10 ** -3, 4, True):
        PI = k * (tf([1], [1]) + tf([1], [T_i, 0]))
        bode(PI, omega=omega, dB=True, Plot=True, label='k = 1, T_i = ' + str(T_i))


@plot('svg/PID.svg')
def pid_regulator():
    k, i = 1, 1
    omega = np.geomspace(10 ** -2, 10 ** 4, 1000, True)
    for T_i, T_d in zip([1, 2 * 0.1, 10 ** -2],
                        [10 ** -2, 0.5 * 0.1, 1]):
        PID = k * (tf([1], [1]) + tf([T_d, 1], [1]) + tf([1], [T_i, 0]))
        bode(PID, omega=omega, dB=True, Plot=True, label='k = 1, T_i = ' + str(T_i) + ', T_d = ' + str(T_d))
        i += 1


@plot('svg/band_pass.svg')
def band_pass():
    T1, T2, T3, T4 = 1, 0.1, 10 ** -8, 10 ** -9
    a = tf([T1, 1], [T2, 1]) * tf([T4, 1], [T3, 1])
    omega = np.geomspace(10 ** -1, 10 ** 10, 1000, True)
    bode(a, omega=omega, dB=True, Plot=True)


fileNames = ['P', 'PD', 'PI', 'PID', 'band_pass']
for fileName in fileNames:
    call(['inkscape -D -z --file=svg/' + fileName + '.svg' +
          ' --export-pdf=' + fileName + '.pdf --export-latex'], shell=True)
plt.show()
