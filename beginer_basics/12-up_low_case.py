#!/usr/bin/python3

string = input("type some lower case to convert to upper case: ")

for i in string:
	if ord(i) >= ord('a') and ord(i) <= ord('z'):#this checks if it is small letter,ord(i) being the value digits of the letter in ASCII table
		i = chr(ord(i) - 32)#This changes the digit to capital letter equivalence;Look at the ASCII table
		print(i, end='')
	else:
		print(i, end='')
