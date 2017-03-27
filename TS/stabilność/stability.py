import matplotlib.pyplot as plt
import numpy as np
from control import pade, bode
from control.matlab import nyquist
from control.matlab import tf, step

a = tf([1, 1], [0.01, 0.5, 3, -10, 10])


def get_axes(x: list, y: list):
    if min(x) > -0.5:
        x_min = min(x)
    else:
        x_min = min(min(x), -1)
    x_max = max(max(x), -1)
    y_min = max(min(min(y), 0), -3)
    y_max = min(max(max(y), 0), 3)
    width = max(x_max - x_min, 1)
    height = max(y_max - y_min, 1)
    return [x_min - 0.05 * width, x_max + 0.05 * width,
            y_min - 0.05 * height, y_max + 0.05 * height]


def curve_length(x, y):
    prev_x = x[0]
    prev_y = y[0]
    length = 0
    for cur_x, cur_y in zip(x[1:], y[1:]):
        length += np.sqrt((cur_x - prev_x) ** 2 + (cur_y - prev_y) ** 2)
        prev_x, prev_y = cur_x, cur_y
    return length


def get_arrow_index(real, imag):
    length = curve_length(real, imag)
    for i in range(1, len(real)):
        if curve_length(real[0:i], imag[0:i]) >= length / 2:
            return i


def get_arrow(real, imag):
    index = get_arrow_index(real, imag)
    arrow_start_x = real[index]
    arrow_start_y = imag[index]
    arrow_end_x = real[index + 1]
    arrow_end_y = imag[index + 1]
    ax = plt.axes()
    ax.arrow(arrow_start_x, arrow_start_y,
             (arrow_end_x - arrow_start_x) * 0.001,
             (arrow_end_y - arrow_start_y) * 0.001,
             head_width=0.0125, head_length=0.025)


def tf2str(transfer_function: tf) -> str:
    name = str(transfer_function)
    name = name.replace('--', '')
    strings = name.split('\n')
    name = ''.join(['\\Huge $\\frac{', strings[1] + '}{', strings[-2], '}$'])
    return 'Nyquist plot'


def plot_nyquist(transfer_function):
    real, imag, freq = nyquist([transfer_function],
                               np.geomspace(10 ** (-10), 10 ** 10, 1000), False)
    plt.figure()
    plt.rc('text', usetex=True)
    plt.plot(real, imag)
    plt.grid()
    plt.axis(get_axes(real, imag))
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    get_arrow(real, imag)
    plt.plot([-1], [0], 'r+')
    plt.title(tf2str(transfer_function))


# print(np.roots([0.01, 0.5, 3, -10, 10]))
# plot_nyquist(a)
# plt.savefig("tex/svg/zad_1_first.svg")
# y, t = step((a * 50).feedback())
# plt.figure()
# plt.plot(t, y)
# degree = 20
# num, den = pade(0.5, degree, numdeg=degree - 1)
# a = tf(num, den) * tf([3], [1, 1])

def real_imag_poly(polynomial: np.poly1d):
    pol = polynomial.coeffs
    rev = [x for x in reversed(pol)]
    sign = 1
    real_ans = []
    imag_ans = []
    for i in range(0, len(rev)):
        if i % 2 == 0:
            real_ans.append(rev[i] * sign)
            imag_ans.append(0)
        else:
            real_ans.append(0)
            imag_ans.append(rev[i] * sign)
            sign *= -1
    real_ans = [x for x in reversed(real_ans)]
    imag_ans = [x for x in reversed(imag_ans)]
    return real_ans, imag_ans


print(real_imag_poly(np.poly1d([1 for x in range(1, 10)])))


def extract_from_poly(num, den):
    numerator = np.poly1d(num)
    num_re, num_im = real_imag_poly(numerator)
    num_re, num_im = np.poly1d(num_re), np.poly1d(num_im)
    denominator = np.poly1d(den)
    den_re, den_im = real_imag_poly(denominator)
    den_re, den_im = np.poly1d(den_re), np.poly1d(den_im)
    multiplier = den_re - den_im * 1j
    new_num = num_re + num_im * 1j
    new_num *= multiplier
    new_num_im = np.poly1d(np.imag(new_num.coeffs))
    roots = np.roots(new_num_im)
    roots = [root for root in roots if root.real >= 0]
    print(roots)
    real_parts = np.polyval(new_num, roots) / \
                 (np.polyval(den_re, roots) *
                  np.polyval(den_re, roots) +
                  np.polyval(den_im, roots) *
                  np.polyval(den_im, roots))
    return np.array([x for x in real_parts.real if x < 0])


#
# real_parts = extract_from_poly([1, 1], [0.01, 0.5, 3, -10, 10])
#
# print([x for x in real_parts.real])
# print([-1 / x for x in real_parts.real])
# for i in range(0, 2):
#     K = - 1 / real_parts[i].real
#     temp_a = a * K
#     y, t = step(temp_a.feedback(), np.arange(0, 30, 0.01))
#     plt.figure()
#     plt.plot(t, y)
#     plt.grid()
#     plt.title('Step response for K=' + str(K))
#     plt.savefig('tex/svg/step' + str(K // 10) + '.svg')
#
# bode([a], dB=True)
# plt.savefig('tex/svg/bode.svg')
#
# real_parts = extract_from_poly([1], [2, 3, 1, 0])
# plot_nyquist(tf([1], [2, 3, 1, 0]))
# print(real_parts)
# plt.savefig('tex/svg/dodatkowe.svg')


num, den = pade(0.5, 10, 9)
delay = tf(num, den)
a = tf([4], [1, 1])
plot_nyquist(a * delay)
plt.savefig('tex/svg/drugie.svg')
plt.show()
