#! /usr/bin/env python
""" decorator.py, by Jan Hamara, 2018-01-10

    This script demonstrates use of decorators

    Example: Make a decorator factory which returns a decorator that decorates functions with one argument.
    The factory should take one argument, a type, and then returns a decorator that makes
    function check if the input is the correct type.
    If it is wrong, it should print("Bad Type").
    Using isinstance(object, type_of_object) or type(object) might help.
"""

def type_check(correct_type):
    def type_check_generator(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
               print('Bad Type')
        return new_function
    return type_check_generator


@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])