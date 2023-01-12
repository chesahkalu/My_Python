#!/usr/bin/python3
#input functions take input from keyboard,with the string in bracket printed when input function is run.
name = input('what is your name you beautiful thang? ')
age = input('what is your age? ')
#print functions prints everything like a string
#{age:d} will cast age as the integer it is and not string. x=hex,b=binary,s=string
print(f'hello, {name} you are {age} year old')

str1 = 'welcome' #to assign string, or print a string always put in parenthesis
str2 = 'to my program'
welcome = str1 + " " + str2 + " " + 3 * "Hurray! " #strings can be concated like this
print(welcome)
