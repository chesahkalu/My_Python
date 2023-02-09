#!/usr/bin/python3

from sub_class import Rectangle
"""here a class Rectangle is imported, it can be inherited from for another class
aswell as some of its methods and attributess manipulated from here"""

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)

try:
    r = Rectangle(10, 2)
    r.width = -10
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
