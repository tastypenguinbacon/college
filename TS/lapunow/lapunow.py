import os
from subprocess import call
from scipy.integrate import ode

import matplotlib.pyplot as plt
import numpy as np

if not os.path.exists('tex/svg'):
    os.makedirs('tex/svg')


def plot(file_name):
    def plot_decorator(f):
        def wrapped():
            plt.figure()
            f()
            plt.legend(loc='lower right', prop={'size': 6})
            plt.savefig('tex/svg/' + file_name, bbox_inches='tight')

        wrapped()
        return wrapped

    return plot_decorator


fileNames = []
for fileName in fileNames:
    call(['inkscape -D -z --file=tex/svg/' + fileName + '.svg' +
          ' --export-pdf=' + fileName + '.pdf --export-latex'], shell=True)


plt.plot([z[0] for z in y], [z[1] for z in y])
plt.show()
