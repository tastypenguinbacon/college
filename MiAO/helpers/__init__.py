from itertools import tee


def pairwise(iterable, skip=1):
    a, b = tee(iterable)
    for i in range(skip):
        next(b)
    return zip(a, b)


def validate(validator):
    def validator_decorator(func):
        def func_wrapper(*args):
            validator(*args)
            return func(*args)

        return func_wrapper

    return validator_decorator
