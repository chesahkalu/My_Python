#!/usr/bin/python3

for i in range(1, 101): #basic looping function in python, the range function creating a range between the two numbers excluding the last.
	if i % 3 == 0 and i % 5 == 0:
		print('fizzbuzz', end=' ')
	elif i % 3 == 0:
		print('fizz', end=' ')
	elif i % 5 == 0:
		print('buzz', end=" ")
	else:
		print(i, end=' ')
