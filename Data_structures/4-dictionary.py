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

#a function def roman_to_int(roman_string): that converts a Roman numeral between 1 to 3999 to an integer
def roman_to_int(roman_string):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_dict[roman_string[i]] > roman_dict[roman_string[i - 1]]:
            result += roman_dict[roman_string[i]] - 2 * roman_dict[roman_string[i - 1]]
        else:
            result += roman_dict[roman_string[i]]
    return result

#a function that returns a key with the biggest integer value.
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    b_score = max(a_dictionary.values(), default=None)
    for k, v in a_dictionary.items():
        if v == b_score:
            return k

#a function that prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary.items())

    for k, v in sorted_dictionary:
        print('{0}: {1}'.format(k, v))

#a function that returns a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()

    for k, v in b_dictionary.items():
        b_dictionary[k] = v * 2

    return b_dictionary



