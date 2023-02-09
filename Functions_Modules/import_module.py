#!/usr/bin/python3



import some_functions # this imports the file that has all the written functions. tthis can be written like below to use a simplier name
from some_functions import interest_rate # this imports only one function from the file module
from some_functions import cipher as ex # this imports function cipher from module some_functions and renamed to ex
adder = __import__("some_functions").adder

"""
we import using the name of the file. Naming a module is crucial. If not named rightly(with "-", or "number")
would cause an error during importation, as it wont be a recognized module"""

print(some_functions.add_int(3,8))

print("--------------------------------")

interest_rate(10000,5,5)

print("--------------------------------")

some_functions.to_upper("I am In LoVe wiTh Jesus")

print("--------------------------------")

ex("I Love you so VERY Much", 10)
