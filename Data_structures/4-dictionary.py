#!/usr/bin/python3

#dictionaries use keys as a form of index, keys in dictionaries store value within the key in the dictionary
#keys can be of any immutable data type like strings,ints and even tuples containing only one data type
#list(d) on a dic. returns a list of all the keys used in dict, in insertion order (if you want it sorted, just use sorted(d) instead).
#To check whether a single key is in the dictionary, use the `in`` keyword.

empty_dict = {}
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)

capital_city["Japan"] = "Tokyo" #add new element to dict.
capital_city["Japan"] = "Home" #change a key value

capital_city["Nigeria"] = "Abuja"

print(capital_city["Japan"])
print(capital_city["Nepal"])

del capital_city["Nigeria"] #remove a key

list(capital_city) #list all keys
sorted(capital_city) #sort keys


dicti = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # creates a dict
print(dicti)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

dict_comprehension = {x: x**2 for x in (2, 4, 6)}
print(dict_comprehension)


#some methods
"""""
all()	Return True if all keys of the dictionary are True (or if the dictionary is empty).
any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
len()	Return the length (the number of items) in the dictionary.
sorted()	Return a new sorted list of keys in the dictionary.
clear()	Removes all items from the dictionary.
keys()	Returns a new object of the dictionary's keys.
values()	Returns a new object of the dictionary's values

"""




