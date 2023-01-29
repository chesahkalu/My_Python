#!/usr/bin/python3

"""in this code we are going to create a class of rectangle,encapsulate its datas attributes,
make the data private(to avoid them from being accidentally modified by other methods and classes),
then create getters(to retrieve the datas) and setters(to change the data). Also, the setters would
function to raise type value errors if the data change is not in accordance to the desired requirement.
We are going to use the datas to to create some methods and perform some funtions"""

class Rectangles:
    def __init__(self, height=0, width=0):
        self.height= height
        self.width= width
        """A class is created, initialization of attributes set for during object creation.
        Remember the use of self, to refer to the object being used during initialization"""

    @property #this is a function used to get the private attribute data of the refered object(property).it creates and return the property of the object
    def height(self):
        return self.__height
        """this is the getter function, that gets the length value and the two underscores return them as private data
        therefore returning __length"""

    @height.setter #the function to change the length attribute while raising some errors if the change isnt in a required form
    def height(self, value):
        """length is set, and value is created to assign to length"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
            """value are given conditions to meet when being set, else errors are raise, if no conditions are required,
            then self's length is just assigned as the data assigned to value, hence data is changed and set"""
        else:
            self.__height = value
            """Now the only way to change the private data is with the set function"""

    #we should go ahead to properly encapsulate other attibutes in this class with getters and setters

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

#classe created. Attributes created and encapsulated with getters and setters.Now is time to create some objects and methods.


    def area(self):
        a = self.__height * self.__width
        return a

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height + self.__width + self.__height + self.__width

rec1 = Rectangles(8,5)
rec2 = Rectangles(8,0)
print(rec1.area())
print(rec1.perimeter())
print(rec2.area())
print(rec2.perimeter())

def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))