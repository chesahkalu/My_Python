#!/usr/bin/python3

while True: #makes the loop last forever
	number = int(input('enter number: '))
	if number > 0 and number < 100:
		print(f"your number is {number}")
	if number > 100:
		continue #used to ignore a condition if true,and continue to the start of the loop.
	if number < 0:
		break #ends the loop and goes to next line of code,if no line, ends program
	if number > 50:
		pass #place holder for future code,skip, put a code later
print('fuck you \n')

pass 

language = ['python','java','swift','c','c++']
for i in language:
	if i == 'swift' or i == 'c++':
		continue
	print(i)
