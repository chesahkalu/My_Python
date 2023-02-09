#!/usr/bin/python3

"""Functions are used to make readable clean code. A function houses lines of code that will easily perfrom an action
when called with some argument variables, instead of always repeating the code in the functions.
Funtions can be used in the same file, making your code shorter and beter.
They can also be called (imported) into another file, in different ways."""

def add_int(x,y):
        return x + y
"""Defines a function called add_int. (x,y) are arguments for the function to work with when it is called.
function will add the two variables x & y passed to it. eg. below"""


if __name__ == "__main__":
    print(add_int(5,10)) #add int called and asked to print whatever it returns

    x = add_int(10,20) #return of add int assigned to X
    print(x) # X printed