from unittest import TestCase

import numpy as np
import matplotlib.pyplot as plt

from algorithms.directional import expansion, golden_ratio


class TestExpansion(TestCase):
    def test_when_quadratic_function_passed_stops_at_minimum(self):
        run = expansion(lambda x: x ** 2, -8, 1, 2)
        self.assertEqual(run[len(run) - 2], 0)

    def test_when_function_is_rising_in_wrong_direction_returns_starting_point_and_first_computed(self):
        run = expansion(lambda x: x, 0, 1, 2)
        self.assertEqual(len(run), 2)

    def test_when_function_has_no_minimum_output_has_length_of_max_steps(self):
        max_iterations = 100
        run = expansion(lambda x: 1 / (x + 1), 0, 1, 2, max_iterations)
        self.assertEqual(len(run), max_iterations)

    def test_when_multidimensional_function_finds_the_minimum(self):
        initial_point = np.array([-8, -8])
        step = np.array([1, 1])
        expansion(lambda x: x.T @ x, initial_point, step, 2)


class TestGoldenRatio(TestCase):
    def test(self):
        result_x = golden_ratio(lambda x: x ** 2, -5, 5, iterations=1000)
        result_y = list(map(lambda x: x * x, result_x))
        x = np.arange(-5, 5, 0.01)
        y = x * x
        plt.plot(result_x, result_y, 'ro')
        plt.plot(x, y)
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Złoty podział!!!")
        plt.show()
