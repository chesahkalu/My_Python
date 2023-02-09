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

    x = add_int(10,20) #return of add_int assigned to X
    print(x) # X printed

    interest_rate(10000,5,5) # interest rate called, no need to print cos printing the outputs is part of the fucntion
