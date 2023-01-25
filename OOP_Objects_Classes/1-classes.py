#!/usr/bin/python3

#classes could be seen as a holder of objects(instances) with related datas(attributes) and functions(methods).
#This classes can be uploaded with so many much datas and functions, and the functions can do so many powerful things with the datas.
#This is the heartline of programming in python
#Also,there are various class features that will help in making classes a more powerful tool in data manipulations, efficacy and usage.

class Users: #A class of users is created, with the class title ALWAYS STARTING WITH CAPITAL LETTERS, and most have a line below(use `pass` if no code yet)
    """This is a class of users, with this we will slowly create a basic,
    but proper class of users with various attributes and methods.
    We will also try to perform multiple features on this classes """#this is called Docstrings, a form of very important documentations about parts of your classes.

    name = ''
    age = 0
    id_no = ''
    height = 0
    company = "Amazon"
    """This are the class (variables) that can be assinged to objects(instance), and also use as a
    general class variable.More attributes can be added to objects, in various ways. Even while creating the objects.
    The attribute values are left empty so that creating objects are still possible without assigning 
    values to them already"""
    
        

    def say_who(self):
        print(f'I am {self.name},I am {self.age} years old and my height is {self.height}cm')
    """This is a function(Method), the (self) is used to make refrence to the object using the function,
    when an object calls the function, it uses the attribute data assigned to the self of that object,
    It uses the variables of the objects it was run with."""

    def __init__(self, name='', age=0, height=0):
        self.name = name #the values in the function arguments are stored to the fields in the attribute(of the object when created )
        self.age = age
        self.height = height
    """The init function. This funtion is used to initialize attribute to object during creation of objects
    self is used to refrence the new object being created."""



user1 = Users()         #now an object is created, by giving it a name and telling the program it is an instance of the class
user1.name = 'Andrew'
user1.age = 20
user1.height = 169    #objects are assigned some attributes, which are now the objects fields. Which are Instance variables.
"""The above is the basic way to create and asign fields data to the attributes of the object. Creating instance varioables."""

user2 = Users("Banarbas", 23, 180) #a second object is created and with the init function the attributes are asigned and initialized to the object during creation.

user1.say_who()#a method is assigned to an object in the class. Method is run and uses the arguments of the object because self was used in creating the arguments.
user2.say_who()
print(Users.company)