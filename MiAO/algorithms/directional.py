from numpy.linalg import norm as vector_length
from numpy.ma import sqrt


def expansion(function, initial_point, initial_step, alpha, max_iterations=10):
    """
    Finds the minimum of the function passed to it, computed using the expansion method

    :param function: the function to minimize
    :param initial_point: the starting point of the methods
    :param initial_step: a vector which searches for the co
    :param alpha: the exponent by which the next step will be computed
    :param max_iterations: maximum number of iterations after which computations are aborted
    :return: a list of (point, value) pairs of intermediate values and the first one that failed
    """
    current_point = initial_point
    direction = initial_step / vector_length(initial_step)
    previous_value = function(initial_point) + 1
    search_history = []
    for i in range(0, max_iterations):
        current_value = function(current_point)
        search_history.append(current_point)
        if current_value >= previous_value:
            return search_history
        current_point = initial_point + direction * initial_step * alpha ** i
        previous_value = current_value
    return search_history


def golden_ratio(function, range_begin, range_end, accuracy=0.01, iterations=10):
    """
    Finds the minimum of the function passed to it, computed using the expansion method

    :param accuracy: the width of the range when computation is stopped
    :param function: the function to minimize
    :param range_begin: the begin of the range
    :param range_end: the end of the range
    :param iterations: the iterations
    :return: a list of (point, value) pairs of intermediate values
    """
    tau = (sqrt(5) - 1) / 2
    width = range_end - range_begin
    if iterations == 0 or width < accuracy:
        return []
    first_point = tau * range_begin + (1 - tau) * range_end
    second_point = (1 - tau) * range_begin + tau * range_end
    if function(first_point) > function(second_point):
        solution_of_rest = golden_ratio(function, first_point, range_end, accuracy, iterations - 1)
        return [first_point] + solution_of_rest
    else:
        solution_of_rest = golden_ratio(function, range_begin, second_point, accuracy, iterations - 1)
        return [second_point] + solution_of_rest
