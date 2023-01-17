#!/usr/bin/python3

#printing small letters
for i in range(97, 123): #decimal ascii value of a-z (remember in range the last range is not printed, so z is number 122)
	print(chr(i), end='') #chr(i) to convert dec to ascii valuei

print()

for i in range(97, 123): #decimal ascii value of a-z
	print(f'{i:c}', end='') #{i:c} converting the format to char, as :d=int, :s=string, :f=float

print()

for i in range(ord('a'), ord('z') + 1 ): #ord converts the char to decimal ascii value(remember range, ordZ wont be printed, so +1 prints it and ignore the last)
	print(i, end=' ')

print()

for i in range(0, 101):
	print(hex(i)) #convert number to hex, print i and then new line
