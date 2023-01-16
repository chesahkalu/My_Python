#!/usr/bin/python3

#tuples are like lists but immutable,hence so many methods that work with list wont work on tuples.

#tuples are inmutable, but this a function that can pass as making a tuple mutable.
#this function will change the value at a given index, hence changing a tuple
#given the the tuple to change, the index and the new value to input
def change_tuple(old,indx,cont):
    return old[:indx] + (cont,) + old[indx+1:]

tup = (1,2,3,'go')
print(tup)
print('index of \'go\' in tup is: ',tup.count('go'))#this method finds the index of a data in tuple
print('value in index 3 is: ',tup.index(3))#finds the value in the given index


#lets try changing index 3 in this tuple, and print a statement if failure
try:
    tup[3] = 'go'
    print(tup)
except:
    print('normally tuples aren\'t mutable :(')

#lets try with the function
tup = (change_tuple(tup,3,'gooo'))
print(tup)

#this are tuples
tup1 = 1,
tup2 = 2,3,4
tup3 = (5,6,7)
tup4 = tup1 + tup2 + tup3 #tupples arent mutable but can be contated. and only with itself,
print(tup3)

#using tupples to swap values
a = 4
b = 6
a,b = b,a

print('a =' , a ,'and' 'b =' , b)

