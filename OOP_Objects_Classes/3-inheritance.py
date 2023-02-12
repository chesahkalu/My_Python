#!/usr/bin/python3

"""class inheritance , simply acquires all the methods and attributes of a class, making it a subclass
and the copied class a super class"""

"""The subclass can aswell be adjusted in different ways, the init
functions of the super class has to be called in the sub class as well as the sub class having its 
own init functions for its attribute."""

"""Methods can be overiden by siply Defining them and rewriting the code in the sub class.
Methods can alsobe referred to by using the super() function to call on them."""

class Polygon:
    def __init__(self, sides):
        self.sides = sides #this would a list of differnt int reping the length of diff side of the polygon
    
    def displayinfo(self):
        print("A polygon is a two-dimensional geometric figure that has a finite number of sides,\
              The sides of a polygon are made of straight line segments connected to each other end to end.\
              Thus, the line segments of a polygon are called sides or edges.")
        
    def get_perimeter(self):
        perimeter = sum(self.sides)

class Rectangle(Polygon): #this is a sub class inheriting all the attributes and methods of Polygon class........
