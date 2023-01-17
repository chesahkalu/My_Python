#!/usr/bin/python3

#sets data are unique and cant be duplicated
#sets when called usually arent in the order of creation hence the cant be indexed
#

set1 = set() #creates an empty set
my_set = {30,40,50,50,40,30,20,10} #when printed or returned, doesnt return any duplicate
print(my_set)

#Set operations
A = {1,3,5,6,7,9,21,43,65,3,17}
B = {42,65,12,5,7,88,21,2,8}
print('Union using |:', A | B) #returns all the element of each set
print('Union using union():', A.union(B)) 

print('Intersection using &:', A & B)#returns data available in both sets
print('Intersection using intersection():', A.intersection(B))

print('Difference using &:', A - B)#return the datas in A that is not in B.
print('Difference using difference():', A.difference(B)) 

print('using ^:', A ^ B)#return data not in both sets
print('using symmetric_difference():', A.symmetric_difference(B)) 


#some methods

# union() method - returns the union of two sets as a new set
set1 = {1, 2, 3}
set2 = {2, 3, 4}
union_set = set1.union(set2)
print(union_set) # {1, 2, 3, 4}

#update() method is used to update the set with items other collection types (lists, tuples, sets, etc)
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)

# add() method - adds an element to the set
my_set.add(1)
print(my_set) # {1}

# clear() method - removes all elements from the set
my_set.clear()
print(my_set) # set()

# copy() method - creates a shallow copy of the set
another_set = {1, 2, 3}
my_set = another_set.copy()
print(my_set) # {1, 2, 3}

# discard() method - removes an element from the set if it is present
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set) # {1, 3}




# difference_update() method - removes elements of another set from this set
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1) # {1}


# intersection_update() method - removes elements not present in both sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1) # {2, 3}

# isdisjoint() method - returns True if two sets have no elements in common
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) # True

# issubset() method - returns True if all elements of a set are present in another set (issubset() is a subset of)
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2)) # True

# issuperset() method - returns True if a set contains all elements of another set (issuperset() is a superset of)
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(set1.issuperset(set2)) # True


# update() method - adds elements of one set to another set
set1 = {1, 2, 3}
set2 = {2, 3, 4}


all()	#Returns True if all elements of the set are true (or if the set is empty).
any()	#Returns True if any element of the set is true. If the set is empty, returns False.
enumerate()	#Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
len()	#Returns the length (the number of items) in the set.
max()	#Returns the largest item in the set.
min()	#Returns the smallest item in the set.
sorted()	#Returns a new sorted list from elements in the set(does not sort the set itself).
sum()	#Returns the sum of all elements in the set.

"""""
add()	#Adds an element to the set
clear()	#Removes all elements from the set
copy()	#Returns a copy of the set
difference()	#Returns the difference of two or more sets as a new set
difference_update()	#Removes all elements of another set from this set
discard()	#Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	#Returns the intersection of two sets as a new set
intersection_update()	#Updates the set with the intersection of itself and another
isdisjoint()	#Returns True if two sets have a null intersection
issubset()	#Returns True if another set contains this set
issuperset()	#Returns True if this set contains another set
pop()	#Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove()	#Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference()	#Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	#Updates a set with the symmetric difference of itself and another
union()	#Returns the union of sets in a new set
update()	#Updates the set with the union of itself and others
"""

