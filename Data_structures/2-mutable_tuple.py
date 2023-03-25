#!/usr/bin/python3

#tuples are like lists but immutable,hence so many methods that work with list wont work on tuples.
#immutability makes them write_protected(the content cant be changed)
#interating tthrough tuples are faster, and they mainly used to store hetrogenous data types
#tuples due to its immutability can be used as keys for dictionary
#tuples can be sliced and indexed- check index_slicing in beginer basics folder

#tuples are immutable, but this a function that can pass as making a tuple mutable.
#this function will change the value at a given index, hence changing a tuple
#given the the tuple to change, the index and the new value to input
def change_tuple(old,indx,cont):
    return old[:indx] + (cont,) + old[indx+1:]

tup = (1,2,3,'go')
print(tup)
'go' in tup #returns true, or false if 'go' is in tup. print function infront of it prints true or false.
print('go' not in tup)
print('index of \'go\' in tup is: ',tup.index('go'))#this method finds the index of a data in tuple, the index of the first data value if the are multiple
print('count of how many \'go\' is: ',tup.count('go'))#finds how many of the particular value is in the tuple, 'go' is just one



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
tup0 = () #empty tuple
tup1 = 1,
tup2 = 2,3,4
tup3 = (5,6,7)
tup4 = tup1 + tup2 + tup3 #tupples arent mutable but can be contated. and only with itself,
tup5 = [tup1,tup2,tup3] #this is a list of tuples
print(tup4)
print(tup5)
print (tup5[2][1]) #this prints the index 1 of the tuple, in the index 2 of the lisst of tuples
print(tup4)

#using tupples to swap values
a = 4
b = 6
a,b = b,a

print('a =' , a ,'and b =' , b)

