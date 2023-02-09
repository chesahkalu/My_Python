#!/usr/bin/python3

from sub_class import Rectangle
"""here a class Rectangle is imported, it can be inherited from for another class
aswell as some of its methods and attributess manipulated from here"""

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)
"""Init method initialized and id attribue for object r3 checked"""

print("--------------------------------")

try:
    r = Rectangle(10, 2)
    r.width = -10
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
"""class setters method validation check"""

print("--------------------------------")

r3 = Rectangle(8, 7, 0, 0, 12)
print(r3.area())
"""area method applied and checked"""

print("--------------------------------")

r1 = Rectangle(4, 6)
r1.display()
"""display method used"""

print("--------------------------------")

r1 = Rectangle(4, 6, 2, 1, 12)
print(r1)
"""str magic method used"""

print("--------------------------------")

r1.update(89, 2, 3, 4, 5)
print(r1)
"""update(*args) method applied and checked"""

print("--------------------------------")

r1.update(y=1, width=2, x=3, id=89)
print(r1)
"""update(**kwargs) method applied anc checked"""


