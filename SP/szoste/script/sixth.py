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

x = []
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
            x.append(float(row[0]))
            U_AC.append(float(row[1]))
            U_DC.append(float(row[2]))


def configure_plot(i=iter(range(1,20))):
    plt.figure(next(i))
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.grid(True)


def abs_error():
    xx = np.array(x[:])
    yy = np.array(U_AC[:])
    for i in range(len(xx)):
        if xx[i] <= 62.2:
            yy[i] *= -1
    a, b = linear_regression(xx, yy)
    calculated = a * xx + b

    configure_plot()
    plt.plot(xx, yy - calculated)
    plt.show()


def uac_x():
    configure_plot()
    plt.plot(x, U_AC, [62.2], [0.02648], 'ro')
    plt.ylabel("{\\Large $\\mathrm{U_{AC}}$ [V]}")
    plt.xlabel("{\\Large x [mm]}")
    plt.savefig("../img/Uac_od_x.png")


def uac_udc():
    configure_plot()
    plt.plot(U_DC, U_AC, [0.001], [0.02648], 'ro')
    plt.ylabel("{\\Large $\\mathrm{U_{AC}}$ [V]}")
    plt.xlabel("{\\Large $\\mathrm{U_{DC}}$ [V]}")
    plt.savefig("../img/Uac_od_Udc.png")


def udc_x():
    configure_plot()
    plt.plot(x, U_DC, [62.2], [0.001], 'ro')
    plt.ylabel("{\\Large $\\mathrm{U_{DC}}$ [V]}")
    plt.xlabel("{\\Large x [mm]}")
    plt.savefig("../img/Udc_od_x.png")


def main():
    if len(sys.argv) != 2:
        raise ValueError('Not enough parameters')
    get_values()
    uac_x()
    abs_error()
    uac_udc()
    udc_x()


if __name__ == '__main__':
    main()
