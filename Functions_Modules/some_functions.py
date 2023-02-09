#!/usr/bin/python3

"""Functions are used to make readable clean code. A function houses lines of code that will easily perfrom an action
when called with some argument variables, instead of always repeating the code in the functions.
Funtions can be used in the same file, making your code shorter and beter.
They can also be called (imported) into another file, in different ways."""

def add_int(x,y):
    return x + y
"""Defines a function called add_int. (x,y) are arguments for the function to work with when it is called.
function will add the two variables x & y passed to it. eg. below"""



def interest_rate(initial,rate,year):    
    print(f"Initial investment = {initial}, for a {year} year period, on a {rate}% return yearly")

    rate = float(rate)/100
    compound = (initial * rate) + initial

    for i in range(year):
        print(f'For {i+1} years your compound return is {compound:.2f}')#converting float compound to 2 decimal place
        compound = (compound * rate) + compound #updates your initial to the current compound
"""Defines a function that takes 3 argument, an initial investment value, the expected rate of return every year
and calculates the total returns every year and prints it."""


def to_upper(string):
    for i in string:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):#this checks if it is small letter,ord(i) being the value digits of the letter in ASCII table
            i = chr(ord(i) - 32)#This changes the digit to capital letter equivalence;Look at the ASCII table
            print(i, end="")
        else:
            print(i, end="")
    print("\n")
"""defines a function that takes a string as argument, it loops throug the string, and any letter
that is a lower case letter, it turns it to a upper casse letter"""




def cipher(message, key):
    for i in message:
        if ord(i) >= 65 and ord(i) <= 90: #checks for uppercase letter, to maintain uppercase
            i = chr(ord(i) + key) #inputs key to cipher and move the letters in key number position
            if ord(i) > 90: #if key ciphers above ascii valu of Z, result wont rotate to continue from A 
                i = chr(ord(i) - 26) # Rotates to start from begining A, instead of continue to take next ASCII value
            print(i, end='')
        
        elif ord(i) >= 97 and ord(i) <= 122:#checks if lowercase letter to maintain
            i = chr(ord(i) + key)
            if ord(i) > 122:
                i = chr(ord(i) - 26)
            print(i, end='')

        else:
            print(i, end='')
    print("\n") 
"""this is a simple program that will code change a written massage to different letterss with a given key.
The key shift the letters by the given number of positions.
The usage of this function can be seen in the function file."""



def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)


def sort_a_list(*args): # the * allows a function to take multiple arguments inform of a tuple,hence a number of argument isnt defined
	list_h =[]
	for i in args: #when used in the function dont include the *
		list_h.append(i)
	list_h.sort()
	print(list_h)
"""we should use an asterisk * before the parameter name to pass variable length arguments.
The arguments are passed as a tuple and these passed arguments make tuple inside the 
function with same name as the parameter excluding asterisk *. So it simply take an argument value into a tuple"""


def intro(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key,value))
"""kwargs on the other allows us to pass the variable length of keyword arguments to the function.
It just allows us to pass multiple arguments in form of a dictionary
of keys and values. We can use **kwargs in a method for a class to change or update attibutes 
to an object."""






if __name__ == "__main__": 
    """ when this particular file is executed, every code runs, including the codes using the functions.
    During this execution the system sees the name of this file as "__main__". This means that the file is
    being run like a script or on the command line.

    when this file is imported for accessing the functions in a command line or in another file,
    the imported file is first run when the file using the function is executed.
    This means thas every code in this file will run. Meaning including the below codes which arent functions.

    We do not want this to happen, we want only the imported file to run the above codes(the functions) in the other file(import_module).
    To stop this from happening, the "If __name == "__main__",  is put above this codes we do not want running.
    This means that this codes will only run , if the program senses that the file is being exectued and run like a script
    
    So when the file is imported, and the file using the the function is run,
    the  program recognises the defined functions, but doesnt run the codes below
    since the file was imported and not being run or executed."""

    print(add_int(5,10)) #add_int called and asked to print whatever it returns

    print("--------------------------------")

    x = add_int(10,20) #return of add_int assigned to X
    print(x) # X printed

    print("--------------------------------")

    interest_rate(10000,5,5) #interest rate called, no need to print cos printing the outputs is part of the fucntion

    print("--------------------------------")

    to_upper("i am very tired")

    print("--------------------------------")

    adder(4,48,39,2,3,45,43,24)

    print("--------------------------------")

    sort_a_list(4,48,39,2,3,45,43,24)

    print("--------------------------------")

    intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)