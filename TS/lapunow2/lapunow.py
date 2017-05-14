import os
from subprocess import call
from time import time

import matplotlib.pyplot as plt

from diff_equations import *
from initial_conditions import init_points_on_rectangle
from plot import fileNames, for_name

if not os.path.exists('tex/svg'):
    os.makedirs('tex/svg')

begin = time()

temp = lambda x: 0.02517517 * x ** 3 + 0.23480313 * x ** 2 - 0.93830795 * x - 4.47556726 if -8 < x < 1 else -255 * x - 6
x = np.linspace(-20, 20, 300)
right = lambda x: temp(x - 2 * np.pi)
more_right = lambda x: right(x - 2 * np.pi)
middle = lambda x: right(x + 2 * np.pi)
left = lambda x: middle(x + 2 * np.pi)
left = np.array(list(map(left, x)))
middle = np.array(list(map(middle, x)))
more_right = np.array(list(map(more_right, x)))
right = np.array(list(map(right, x)))
height, width = 10, 20

width, height = 3, 3
for_name("first", width, height)(
    lambda t, y: first_system(y),
    lambda: init_points_on_rectangle(width, height, 800)
)

tex_image_format = """
\\begin{figure}[H]
    \\centering
    \\def \\svgwidth{0.7\\columnwidth}
    \\input{%s.pdf_tex}
    \\caption{TODO}
\\end{figure}\\noindent
"""
with open('tex/temp.tex', mode='w') as temp_tex:
    for fileName in fileNames:
        call(['inkscape -D -z --file=tex/svg/' + fileName + '.svg' +
              ' --export-pdf=tex/' + fileName + '.pdf --export-latex'], shell=True)
        print(tex_image_format % fileName, file=temp_tex)

end = time()
print(end - begin)
