#!/usr/bin/python3

for i in range(10): #prints 0-9
	print(i)

for i in range(1, 10): #the last number isnt printed
	print(i, end=' ')
print()

#skip one in range
for i in range(1, 10, 2):
	print(i, end=' ')
print()

#in reverse
for i in range(10, 0, -1):
	print(i, end=' ')
