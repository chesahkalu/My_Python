#!/usr/bin/python3

import random #imports a function to create random variables

#a function that creates a list of 5 random numbers

randomlist=[] #creates and empty list first,
for i in range(5): #does the code under 5 times
	randomlist.append(random.randrange(2,50)) #append adds to the list. It adds random number generated between 2-50 with random.range

for i in randomlist:
	print(i, end=' , ')
print()
print(randomlist)

print()

for i in reversed(randomlist): #reverses random list
	print(i, end=' , ')

print()

newrandomlist= [random.randrange(2,50) for x in range(5)]#a concise way of creating a list(list comprehension)

for i in newrandomlist:
	print(i, end=' , ')
print()
print(newrandomlist)


 