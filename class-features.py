#! /usr/bin/env python
""" class-features.py, by Jan Hamara, 2018-01-10

    This script demonstrates structural organisation of class methods and dunder functions
"""

# top-level function or top-level syntax => corresponding __
#   x + y       ->      __add__
#   init x      ->      __init__        (constructor)
#   repr(x)     ->      __repr__

import sys

class Polynomial:

    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x,y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)


p1 = Polynomial(1, 2, 3)    # x2 + 2x + 3
p2 = Polynomial(3, 4, 3)    # 3x2 + 2x + 3

print(sys.path)


