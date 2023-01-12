#!/usr/bin/python3

height = int(input('Input pine tree height: '))

space = height - 1
base = 1
base_space = height - 1

while height != 0:
	for i in range(space):
		print(' ', end='') #end='' , stopes a code out put moving to new line. it ends on same line at end of print
	for i in range(base):
		print('#', end='') #end='' , so # wont print vertically, it prints horizontally
	print() #this prints a new line
	
	space = space - 1
	base = base + 2
	height = height - 1

for i in range(base_space):
	print(' ', end='')
print('#')
