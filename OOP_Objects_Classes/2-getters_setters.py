#!/usr/bin/python3

"""in this code we are going to create a class of rectangle,encapsulate its datas attributes,
make the data private(to avoid them from being accidentally modified by other methods and classes),
then create getters(to retrieve the datas) and setters(to change the data). Also, the setters would
function to raise type value errors if the data change is not in accordance to the desired requirement.
We are going to use the datas to to create some methods and perform some funtions"""

class Rectangles:
    def __init__(self, length=0, width=0):
        self.length= length
        self.width= width
        """A class is created, initialization of attributes set for during object creation.
        Remember the use of self, to refer to the object being used during initialization"""

    @property #this is a function used to get the private attribute data of the refered object(property).it creates and return the property of the object
    def length(self):
        return self.__length
        """this is the getter function, that gets the length value and the two underscores return them as private data
        therefore returning __length"""

    @length.setter #the function to change the length attribute while raising some errors if the change isnt in a required form
    def length(self, value):
        """length is set, and value is created to assing to length"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
            """value are given conditions to meet when being set, else errors are raise, if no conditions are required,
            then self's length is just assigned as the data assigned to value, hence data is changed and set"""
        else:
            self._length = value
            """Now the only way to change the private data is with the set function. Using the inittialization function at object creation
            will cause an error"""

    #we should go ahead to properly encapsulate other attibutes in this class with getters and setters

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be a positive number")
        else:
            self.__width = value

#classe created. Attributes created and encapsulated with getters and setters.Now is time to create some objects and methods.






