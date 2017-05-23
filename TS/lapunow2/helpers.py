from itertools import tee


def pairwise(iterable, skip=1):
    a, b = tee(iterable)
    for i in range(skip):
        next(b)
    return zip(a, b)


class MyLittleMapper(object):
    def __init__(self, to_map, remembered=None, mapper=lambda x: x):
        self.mapper = mapper
        self.to_map = to_map
        self.remembered = remembered

    def map(self, mapper):
        return MyLittleMapper(self.to_map, self.remembered, lambda x: mapper(self.mapper(x)))

    def apply(self):
        to_map, self.to_map = self.to_map, []
        for e in to_map:
            self.to_map.append(self.mapper(e))
        return self

    def get(self):
        self.apply()
        return self.to_map[:]

    def remember(self):
        self.remembered = self
        return self

    def rewind(self):
        return self.remembered

    def peek(self, peeker):
        peeker(self.to_map)
        return self
