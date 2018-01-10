#! /usr/bin/env python
""" closure.py, by Jan Hamara, 2018-01-10

    This script demonstrates use of closure
"""

def multiplier_of(n):
    def multiply(number):
        return n*number
    return multiply

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))