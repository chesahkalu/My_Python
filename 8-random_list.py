#!/usr/bin/python3

import random #imports a function to create random variables

#a function that creates a list of 5 random numbers

randomlist=[] #creates and empty list first,
for i in range(5): #does the code under 5 times
	randomlist.append(random.randrange(2,50)) #append adds to the list. It adds random number generated between 2-50 with random.range

for i in randomlist:
	print(i)

print()

for i in reversed(randomlist): #reverses random list
	print(i)
