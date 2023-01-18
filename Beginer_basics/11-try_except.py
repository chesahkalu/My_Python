#!/usr/bin/python3
#try exceept functions tries a code, and if error returns a value. It checks if a code would work
#can be used to check for inputs, define accuracy, etc. it is like if/else, but it checks for error code
#The try block lets you test a block of code for errors. The except block lets you handle the error.

try: #tries the code
    number = int(input("please enter only a number: ")) #this can only convert a string in number format to int. it cant convert a char string to int
except: #if it doesnt work, meaning an exception error occured, meaning we put in a string that isnt a number
    print('That is not a number') #executes this code, the code is skipped if no errors 


#we cant be sure the exception error occuring was because it isnt an int inputed. Hence different inbuilt python exceptions can be checked.
#then a code generated according to the exception.

try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")#this wont be printed as the ZeroDivisionError didnt occur
    
except IndexError:
    print("Index Out of Bound.")#this will be executed as there is an index error, because there is no index 5

    #An Else block can be included to execute if no exceptions errors
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0 #assert key word checks if code returns true, if not an exception error called AssertionError is raised
except:
    print("Not an even number!")
else:   #if no errors the below code executes
    reciprocal = 1/num
    print(reciprocal)

