#!/usr/bin/python3
#line 3 collects 3 inputs after prompting the input message. 
num1, ops, num2 = input('input your calculation with a space after each input  ').split()#the split function splits an input as different if it senses a space after each input
num1 = int(num1) #this changes the variable which was inputed and saved as a string to and int
num2 = int(num2)

if ops == '*':
	answ = num1 * num2
	print(f'{num1} * {num2} = {answ}\n')
elif ops == '+':
	answ = num1 + num2
	print(f'{num1} + {num2} = {answ}\n')
elif ops == '-':
         answ = num1 - num2
         print(f'{num1} - {num2} = {answ}\n')
elif ops == '/':
         answ = num1 / num2
         print(f'{num1} / {num2} = {answ}\n')
