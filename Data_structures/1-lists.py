#!/usr/bin/python3

#Lists can be sliced,indexed,change,appended,etc etc.
#Lists are the most flexible data structures

my_list= []# empty list created
my_list2 = ['a', 3.15, 'I love you', 45, 'peace']

for i in range(10):
    my_list.append(i)#loops through range of 5, and adds from 1 - 5 into the python list

print(my_list)
print(my_list2)

print(my_list2[0])
my_list2[2] = 'fuck you'
del my_list[4]
print(my_list2)

#some other methods

# append() method
# Adds an element to the end of the list
my_list.append(6)

# extend() method
# Adds all elements of an iterable to the end of the list
my_list.extend([7, 8, 9])

# insert() method
# Inserts an element at a specific position in the list
my_list.insert(3, 0)

# remove() method
# Removes the first occurrence of a specific element from the list
my_list.remove(5)

# pop() method
# Removes and returns the element at a specific position in the list
last_element = my_list.pop()

# index() method
# Returns the index of the first occurrence of a specific element in the list
index = my_list.index(3)

# count() method
# Returns the number of occurrences of a specific element in the list
count = my_list.count(2)

# sort() method
# Sorts the elements of the list in ascending order
my_list.sort()

# reverse() method
# Reverses the order of the elements in the list
my_list.reverse()

# clear() method
# Removes all elements from the list
my_list.clear()

#some tasks
#Write a function that deletes the item at a specific position in a list.
#Write a function that finds all multiples of 2 in a list.
#Write a function that finds the biggest integer of a list.
#Write a function that retrieves an element from a list like in C.


