#!/usr/bin/env python3
"""
The first parameter passed to the script should be the script directory of the
csv file containing the data to the
"""
import csv
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

length = []
U_AC = []
U_DC = []


def linear_regression(x, y):
    slope, intercept, _, _, _ = stats.linregress(x, y)
    return slope, intercept


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_values():
    with open(sys.argv[1]) as csv_file:
        reader = csv.reader(csv_file, dialect='excel')
        for row in reader:
            if not is_number(row[0]):
                continue
            length.append(float(row[0]))
            U_AC.append(float(row[1]))
            U_DC.append(float(row[2]))


def configure_plot(i=iter(range(1,20))):
    plt.figure(next(i))
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.grid(True)


def abs_error(x, y, swap_point=-1000000.0):
    xx = np.array(x[:])
    yy = np.array(y[:])
    for i in range(len(xx)):
        if xx[i] <= swap_point:
            yy[i] *= -1
    a, b = linear_regression(xx, yy)
    calculated = a * xx + b
    nonlinear = max(abs(yy - calculated)) / (max(yy) - min(yy))
    print("Max error %f" % nonlinear)
    return yy - calculated


def uac_x():
    configure_plot()
    plt.plot(length, U_AC, [62.2], [0.02648], 'ro')
    plt.ylabel("{\\Large $\\mathrm{U_{AC}}$ [V]}")
    plt.xlabel("{\\Large x [mm]}")
    plt.savefig("../img/Uac_od_x.png")
    configure_plot()
    error = abs_error(length, U_AC, 62.2) * 1000
    plt.plot(length, error)
    plt.ylabel("{\\Large $\\mathrm{\\Delta_U$ [mV]}")
    plt.xlabel("{\\Large x [mm]}")
    plt.savefig("../img/Uac_blad.png")


def uac_udc():
    configure_plot()
    plt.plot(U_DC, U_AC, [0.001], [0.02648], 'ro')
    plt.ylabel("{\\Large $\\mathrm{U_{AC}}$ [V]}")
    plt.xlabel("{\\Large $\\mathrm{U_{DC}}$ [V]}")
    plt.savefig("../img/Uac_od_Udc.png")
    configure_plot()
    error = abs_error(U_DC, U_AC, 0.001) * 1000
    plt.plot(U_DC, error)
    plt.ylabel("{\\Large $\\mathrm{\\Delta_U$ [mV]}")
    plt.xlabel("{\\Large $\\mathrm{U_{DC}}$ [V]}")
    plt.savefig("../img/Uac_Udc_blad.png")


def udc_x():
    configure_plot()
    plt.plot(length, U_DC, [62.2], [0.001], 'ro')
    plt.ylabel("{\\Large $\\mathrm{U_{DC}}$ [V]}")
    plt.xlabel("{\\Large x [mm]}")
    plt.savefig("../img/Udc_od_x.png")
    configure_plot()
    error = abs_error(length, U_DC) * 1000
    plt.plot(length, error)
    plt.ylabel("{\\Large $\\mathrm{\\Delta_U$ [mV]}")
    plt.xlabel("{\\Large x [mm]}")
    plt.savefig("../img/Udc_blad.png")


def main():
    if len(sys.argv) != 2:
        raise ValueError('Not enough parameters')
    get_values()
    uac_x()
    uac_udc()
    udc_x()


if __name__ == '__main__':
    main()
