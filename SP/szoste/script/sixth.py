#!/usr/bin/env python3

import csv
import sys
import matplotlib.pyplot as plt

x = []
U_AC = []
U_DC = []


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
            if is_number(row[0]):
                x.append(row[0])
                U_AC.append(row[1])
                U_DC.append(row[2])


def plot1():
    plt.figure(1)
    plt.plot(x, U_DC)
    plt.show()


def plot2():
    plt.figure(2)
    plt.plot(U_DC, U_AC)
    plt.show()

def plot3():
    plt.figure(3)
    plt.plot(x, U_AC)


def main():
    if len(sys.argv) != 2:
        raise ValueError('Not enough parameters')
    get_values()
    plot1()
    plot2()
    plot3()


if __name__ == '__main__':
    main()
    print(x)
    print(U_AC)
    print(U_DC)
