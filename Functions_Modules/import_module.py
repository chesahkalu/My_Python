#!/usr/bin/python3

"""We can import all there is in another file module, including variable, functions and class into another module
Just import the file name, and access the object with a dot(.) notation after the object"""


import some_functions # this imports the file that has all the written functions. this can be written like below to use a simplier name
import some_functions as sm
from some_functions import interest_rate # this imports only one function from the file module 
from some_functions import cipher as ex # this imports function cipher from module some_functions and renamed to ex
ad = __import__("some_functions").adder # this is another way of importing a function from a module, ostly used when module name is conventional,imports adder ass ad.
from some_functions import intro # this is how to import from a different directory 
import Functions_Modules.some_functions 

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

ad(2,45,33,21,9,25,59,48,94,38,29,56)

print("--------------------------------")

sm.sort_a_list(2,45,33,21,9,25,59,48,94,38,29,56)

print("--------------------------------")

intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)