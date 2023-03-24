#!/usr/bin/python3

"""class inheritance , simply acquires all the methods and attributes of a class, making it a subclass
and the copied class a super class"""

"""The subclass can aswell be adjusted in different ways, the init
functions of the super class has to be called in the sub class as well as the sub class having its 
own init functions for its attribute."""

"""Methods can be overiden by simply Defining them and rewriting the code in the sub class.
Methods can also be referred to by using the super() function to call on them."""

class Animal:

    # attribute and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)

# create an object of the subclass
labrador = Dog()

# access superclass attribute and method 
labrador.name = "Rohu"
labrador.eat()

# call subclass method 
labrador.display()