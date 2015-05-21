

import math


class Vector(object):

    def __init__(self, *args):
        self.coords = args

    def __str__(self):
        return str(self.coords)

    def __add__(self, other):
        coords = tuple(map(sum, zip(self.coords, other.coords)))
        return Vector(*coords)

    def __abs__(self):
        return math.sqrt(sum(pow(x, 2) for x in self.coords))

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, index):
        return self.coords[index]

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print abs(v1)
print v1 + v2
print v2[1]
print v2.coords[1]
