import os
from collections import namedtuple

import matplotlib.pyplot as plt

PlotData = namedtuple('PlotData', ['x', 'y'])


class Plot(object):
    def __init__(self, height, width):
        self.figure = plt.figure()
        self.subplots = {}
        self.width = width
        self.height = height
        self.file_name = ''
        for i in range(width * height):
            vertical, horizontal = i // width + 1, i % width + 1
            index = (vertical, horizontal)
            self.subplots[index] = self.figure.add_subplot(height, width, i + 1)

    def plot(self, i, j, data, *args, **kwargs):
        subplot = self.subplots[(i, j)]
        subplot.plot(data.x, data.y, *args, **kwargs)
        return self

    def decorate_subplot(self, i, j, subplot_modifier):
        subplot_modifier(self.subplots[(i, j)])
        return self

    def save(self, name, *args, **kwargs):
        path_elements = name.split('/')[:-1]
        path = '/'.join(path_elements)
        if not os.path.exists(path):
            os.makedirs(path)
        self.file_name = name.split('.')[0]
        self.figure.savefig(name, bbox_inches='tight', *args, **kwargs)
        return self

    def show(self):
        plt.show()
        return self

    def close(self):
        plt.close(self.figure)


def grid(is_enabled):
    return lambda s: s.grid(is_enabled)


def title(title):
    return lambda s: s.title.set_text(title)


def axis(axis):
    return lambda s: s.axis(axis)


def plot_arrow(arrow, *args, **kwargs):
    return lambda subplot: subplot.arrow(arrow.x, arrow.y, arrow.len_x, arrow.len_y, *args, **kwargs)
