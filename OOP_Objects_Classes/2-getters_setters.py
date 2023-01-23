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
        """this is the getter funtion, that gets the length value and the two underscores return them as private data"""




