#! /usr/bin/env python
""" partial.py, by Jan Hamara, 2018-01-10

    This script demonstrates use of partial function
"""

from functools import partial


def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x

part = partial(func, 5, 5, 1)

print(part(23))