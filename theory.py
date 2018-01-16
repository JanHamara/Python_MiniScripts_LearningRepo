#! /usr/bin/env python
""" theory.py, by Jan Hamara, 2018-01-10

    This script demonstrates in code
    the documentation of basic methods in Python
"""



# --------------------------------------------------------------------

#
# Modules & Packages
#

# --------------------------------------------------------------------

# Importing modules and packages always at the start of file
import regex as re
import numpy as np
import pandas as pd
import mock
import importlib as implib
from ..py_packege import main

import random.randint
from random import randint as random_number

number = random_number(10)

# We can look for which functions are implemented in each module by using the dir function
dir(random)

# We can read about it more using the help function
help(randint)

# Reload module
implib.reload('numpy')


# Packages

# Each package in Python is a directory which MUST contain a special file called __init__.py. 
# This file can be empty, and it indicates that the directory it contains is a Python package, 
# so it can be imported the same way a module can be imported.

# The __init__.py file can also decide which modules the package exports as the API, 
# while keeping other modules internal, by overriding the __all__ variable

__all__ = ['randint']



# --------------------------------------------------------------------


# The keyword argument end can be used to avoid the newline after the output,
# or end the output with a different string.
print('Hello World')
print('Enter number', end=" ")



# --------------------------------------------------------------------

#
# Variables
#

# --------------------------------------------------------------------

# You do not need to declare variables before using them, or declare their type. 
# Every variable in Python is an object.

my_int = 7								# integer
my_float = 7.0							# float
my_float = float(7)
my_str = 'Hello'						# string
my_list = ['a', 'b', 'c']				# list
my_set = 7			# integer



#
# Format Conversion
#

value = '100'

int(value)
float(value)
str(value)
repr(value)								# Interpreter readable
list(range(x,y))						# Takes iterable



# Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = 3, 4

# Using two multiplication symbols makes a power relationship
squared = 7 ** 2
cubed = 2 ** 3

# Mixing operators between numbers and strings is not supported!



# --------------------------------------------------------------------

#
# Strings
#

# --------------------------------------------------------------------

len(string)						# Length of object
mystring.index('o')				# Return first position of queried string
mystring[3:7]					# Slice out substring from a to b-1
								# General form: [start:stop:step]

mystring[::-1]					# Reverse string

mystring.lower()
mystring.upper()

mystring.startswith(string)		# boolean
mystring.endswith(string)		# boolean

mystring.split(' ')				# Converts string to list of strings based on condition
								# This one splits at each space


#
# String Formatting
#

# Python uses C-style string formatting to create new, formatted strings. 
name = 'John'
string_f = "Hello, %s!" % name

%s 			# string (or any object with string representation)
%d 			# integers
%f 			# floating point numbers

%.<number of digits>f 			# set fixed amount of digits

%x/%X 		# integers in hex representation (lowercase / uppercase)



# --------------------------------------------------------------------

#
# Lists
#

# --------------------------------------------------------------------

len()
mylist.append()					# Append value to the end of the list
mylist.extend(iterable)			# Extend the list by appending all items from iterable
mylist.insert(0, item)			# Insert an item at given (position, item)
mylist.remove(item)				# Remove the first item in the list
mylist.pop(0)					# Remove the item at given position
								# With no index specified, remove the last item

mylist.clear()					# Remove all items from the list
mylist.index(item)				# Return zero based index of first item found
								# [item, start, end]

mylist.count(item)				# Return the number of occurences of the item in the list

mylist.sort(key = None, reverse = False)		# Sort items of the list
mylist.reverse()
mylist.copy()					# Equivalent to a[:]


# Using lists as Stacks
Use .append() and .pop() method, to treat lists like stacks


# Using lists as Queues
To implement a queue, use collections.deque() 
which was designed to have fast appends and pops from both ends.

from collections import deque

queue = deque(mylist)
queue.append('Terry')				# Terry arrives
queue.popleft()						# First to arrive, now leaves


# When looping through a sequence, the position index and corresponding value 
# can be retrieved at the same time using the enumerate() function.

sequence = ['tic', 'tac', 'toe']

for x, y in enumerate(sequence):
	print(x, y)


# Looping over multiple sequences

for q, a in zip(questions, answers):
	print('Question: {0} /n Answer: {1}'.format{q,a})


reversed()							# Loop over sequence in other direction
sorted()							# Loop over sequence in sorted order



# --------------------------------------------------------------------

#
# Statements
#

# --------------------------------------------------------------------

# if

if condition:
	pass
elif condition2:
	pass
else:
	pass


# while

while condition:
	pass


# for

for x in list:
	pass


for i in range(len(a)):						# Iterate over indices of a sequence
	print(i, a[i])


#
# range()
#

# In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t. 
# It is an object which returns the successive items of the desired sequence when you iterate over it, 
# but it doesn’t really make the list, thus saving space.

# We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something 
# from which they can obtain successive items until the supply is exhausted. 

range(5, 10)								# 5, 6, 7, 8, 9

range(0 ,10 , 3)							# 0 ,3 6, 9

list(range(5))								# This is iterable too



#
# break & continue
#

break 										# Breaks out of the innermost enclosing for or while loop.
continue 									# Continues with the next iteration of the loop.

# Loop statements may have an else clause. 
# It is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), 
# but not when the loop is terminated by a break statement.

for i in range(2):
	pass
else:
	pass


#
# Other Conditions
#

if 'name' not in database:
	pass

if fib_generator() is not types.GeneratorType:
	pass

if a < b == c and not B == C 				# Chained comparisons
											
											# NOT has the highest priority and OR the lowest



# --------------------------------------------------------------------

#
# Functions
#

# --------------------------------------------------------------------

def my_function(pos_arg1, pos_arg2, default = 'hi', *args, **kwargs):
	# some code

	return something


# It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined.


# Default Argument Values
def user_login(user_id, user_pass, verified = 'false'):
	pass


# Keyword Arguments
def create_user(company_id='120392', base_salary='30000')


# *args / **kwargs

def add_items(category, *args, *keywords)
# call as

add_items('technology', 'Panasonic GH4', 'Canon 3D Mark II', type = 'Mirrorless')

# first positional argument goes to defined formal argument 'category'
# all other positional arguments go to *args
# any keyword arguments passed with function go to **keywords


# In the same fashion, dictionaries can deliver keyword arguments with the **-operator
entry234 = {voltage: 1000, volume: 2504, Hz: 20001}
save_meter_data(**entry234)


# Lambda Expressions

# Small anonymous functions can be created with the lambda keyword. 
# This function returns the sum of its two arguments: 
lambda a, b: a+b


# Function annotations (Python Typescript)

def f(arg1: str, arg2: int) -> str:
	"""
		This is a docstring that should defines in one sentence what function does.

		If there is more description or rules, write them in paragraph here, 
		one line break after the header of the docstring.
	"""

    print('I return string')
	print('Annotations: ', f.__annotations__)



# --------------------------------------------------------------------

#
# Classes
#

# --------------------------------------------------------------------

class Person():
	name = 'Janci'										# Property

	def __init__(self, name, age):						# Constructor
		this.name = name
		this.age = age

    def speak(message = 'Hello'):						# Method
    	print(message)


person1 = Person('Agne', 21)							# Instantiation
person1.speak()											# Attribute reference



# --------------------------------------------------------------------

#
# Dictionaries
#

# --------------------------------------------------------------------

dict = {'key1': 'value', 'key2': 'value2', 'key3': 3}

dict['key4'] = 254
del dict['key2']


# Iterating over dictionary
for key, value in dict.items():
    print("Key: %s, Value: %s" % (key, value))


# List all keys
list(dict.keys())


# Constructor
dict([(key, value), (key, value), ..])
# or
dict(key = value, key = value, ..)


# Dictionary Comprehensions
{x: x**2 for x in (2, 4, 6)}

# --------------------------------------------------------------------



# --------------------------------------------------------------------

#
# Advanced Features
#

# --------------------------------------------------------------------



# __main__ condition

# run script only when run directly (as '__main__') not when imported

def main():
	pass

if __name__ == ‘__main__’:
	main()



# --------------------------------------------------------------------

#
# Numpy Arrays
#

# --------------------------------------------------------------------

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Calculate bmi for each array entry with single expression
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)


# Subsetting

print(bmi[bmi < 23])



# --------------------------------------------------------------------

#
# Pandas DataFrames
#

# --------------------------------------------------------------------

# DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.

dict = {
       "country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
}

brics = pd.DataFrame(dict)

print(brics)


# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Importing CVS file
pd.read_csv(‘’file.csv’’)


# Indexing DataFrames

# single bracket						output = Pandas Series
# double bracket	 					output = Pandas DataFrame

print(brics['country'])					# Returns column as Object			
print(brics[['country', 'area']])		# Returns columns as DataFrame			

print(brics[0:4])						# Returns rows (observations)

# loc / iloc

# loc is label-based, which means that you have to specify rows and columns 
# based on their row and column labels.
print(brics.loc[‘BR’, ‘IN’])	

# iloc is integer index based, so you have to specify rows and columns 
# by their integer index like you did in the previous exercise.
print(brics.iloc[0])



# --------------------------------------------------------------------

#
# Generators
#

# --------------------------------------------------------------------

# Generators are used to create iterators, but with a different approach. 
# Generators are simple functions which return an iterable set of items, 
# one at a time, in a special way.

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" % (random_number))

# --------------------------------------------------------------------

def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


fib()

counter = 0
for n in fib():
	print(n)
    counter += 1
    if counter == 10:
        break



# --------------------------------------------------------------------

#
# List Comprehensions
#

# --------------------------------------------------------------------

# List Comprehensions is a very powerful tool, which creates a new list 
# based on another list, in a single, readable line.

word_lengths = [len(word) for word in words if word != "the"]

# Nested list comprehensions

matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
   ]

[[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# In the real world, you should prefer built-in functions to complex flow statements.
# zip()

list(zip(*matrix))



# --------------------------------------------------------------------

#
# Tuples
#

# --------------------------------------------------------------------

# Tuple is another sequence data type, almost exactly same as list
# Tuples are enclosed in parentheses and can be nested
# Tuples are immutable

tuple = "first", "second", "third"

# empty
empty_tuple = ()

# one element
one_el_tuple = "singleton",

# Unpacking tuple
a, b, c = tuple



# --------------------------------------------------------------------

#
# Regular Expressions
#

# --------------------------------------------------------------------


# Regular expressions are a tool for matching patterns in text.

example_regex = r"^(From|To|Cc).*?python-list@python.org"

^ 				# Matches text at the beginning of a line
(From|To|Cc)	# The line has to start with one of the words that are separated by the pipe |
. 				# Dot character means any non-newline character	
*				# This means to repeat 0 or more times
?				# Question character makes it un-greedy

# Slight optimisation
pattern = re.compile(r"\[(on|off)\]") 

# Search for pattern					..in this case [on] or [off]
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))

# Mail Regex
mail_regex = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"



# --------------------------------------------------------------------

#
# Exception Handling
#

# --------------------------------------------------------------------


# Python's solution to errors are exceptions.

# But sometimes you don't want exceptions to completely stop the program. 
# You might want to do something special when an exception is raised. 
# This is done in a try/except block.

try:
	pass
except TypeError:
	pass

# --------------------------------------------------------------------

def do_stuff_with_number(n):
    print(n)

the_list = (1, 2, 3, 4, 5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError:
    	# Raised when accessing a non-existing index of a list
        do_stuff_with_number(0)



# --------------------------------------------------------------------

#
# Sets
#

# --------------------------------------------------------------------

# Sets are lists with no duplicate entries

print(set("my name is Eric and Eric is my name".split()))
# returns [“my”, “name”, “is”, “Eric”, “and”]

# Curly braces or the set() function can be used to create sets. 
# Note: to create an empty set you have to use set(), not {}.. 
# ..the latter creates an empty dictionary

# They are mainly intended to be used for mathematical operations such as union or difference

set1 = ('a', 'b', 'c')
set2 = ('b', 'd')

print(set1.union(set2))									# a, b, c, d 
print(set1.intersection(set2))							# b

# Returns elements that are only in one set
print(set1.symmetric_difference(set2))					# a, c, d

# Returns elements that are in one set and not the other
# a - b
print(set1.difference(set2))							# a, c


# Set Comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}		# {'r', 'd'}



# --------------------------------------------------------------------

#
# Serialization / JSON
#

# --------------------------------------------------------------------

# Python provides built-in JSON libraries to encode and decode JSON.
# There are two basic formats for JSON data. 
# Either in a string or the object data structure. 

# Load JSON from string into object data structure
data = json.loads(json_string)

# Convert JSON from object data structure into string
json_string = json.dumps(data)



# --------------------------------------------------------------------

#
# Partial Functions
#

# --------------------------------------------------------------------

# You can create partial functions in python by using the partial function 
# from the functools library.

from functools import partial

# Partial functions allow one to derive a function with x parameters 
# to a function with fewer parameters and fixed values 
# set for the more limited function.

def multiply(a,b):
	return a*b

double = partial(multiply, 2)

double(4)							# returns 8



# --------------------------------------------------------------------

#
# Code Introspection
#

# --------------------------------------------------------------------

# Code introspection is the ability to examine classes, functions and keywords 
# to know what they are, what they do and what they know.

help()					# Find what does a function or method do

dir() 					# Lists which names a module defines.
						# Note that it lists all types of names: variables, modules, functions..

						# It does not list the names of built-in functions and variables. If you want a list of those, 
						# they are defined in the standard module called 'builtins'


hasattr(object, name)	# eturn whether the object has an attribute with the given name

id(object)				# Return the identity of an object.  
						# This is guaranteed to be unique among simultaneously existing objects.  

type(object) 			# Object’s type

repr()					# Return the canonical string representation of the object.

callable()				# Return whether the object is callable (i.e., some kind of function).
    					# Note that classes are callable, as are instances with a __call__() method.

issubclass(C,B)			# Return whether class C is a subclass (i.e., a derived class) of class B.


isinstance()			# Return whether an object is an instance of a class or of a subclass thereof. 
						# With a type as second argument, return whether that is the object's type.

__doc__ 				# docstring holder

__name__ 				# namespace holder



# --------------------------------------------------------------------

#
# Closures
#

# --------------------------------------------------------------------

# A closure is a function object that remembers values in enclosing scopes even if they are not present in memory. 

# It's very important to note that the nested functions can access the variables of the enclosing scope. 
# However, at least in Python, they are only readonly.
# However, one can use the nonlocal keyword explicitly with these variables in order to modify them.

















