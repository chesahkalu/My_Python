#!/usr/bin/python3
#try exceept functions tries a code, and if error returns a value. It checks if a code would work
#can be used to check for inputs, define accuracy, etc. it is like if/else, but it checks for error code
#The try block lets you test a block of code for errors. The except block lets you handle the error.

try: #tries the code
    number = int(input("please enter only a number: ")) #this can only convert a string in number format to int. it cant convert a char string to int
except: #if it doesnt work, meaning an error occured, meaning we put in a string that isnt a number
    print('That is not a number: ')
