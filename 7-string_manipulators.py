# Strings have many methods we can use beyond what I covered last time
rand_string = "   this is an important string   "
 
# Delete whitespace on left
rand_string = rand_string.lstrip()
 
# Delete whitespace on right
rand_string = rand_string.rstrip()
 
# Delete whitespace on right and left
rand_string = rand_string.strip()
 
# Capitalize the 1st letter
print(rand_string.capitalize())
 
# Capitalize every letter
print(rand_string.upper())
 
# lowercase all letters
print(rand_string.lower())
 
# Turn a list into a string and separate items with the defined
# separator
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))
 
# Convert a string into a list
a_list_2 = rand_string.split()
 
for i in a_list_2:
    print(i)
 
# Count how many times a string occurs in a string
print("How many is :", rand_string.count("is"))
 
# Get index of matching string
print("Where is string :", rand_string.find("string"))
 
# Replace a substring
print(rand_string.replace("an ", "a kind of "))
 
# ---------- PROBLEM : ACRONYM GENERATOR ----------
# You will enter a string and then convert it to an acronym
# with uppercase letters like this
'''
Convert to Acronym : Random Access Memory
RAM
'''
 
# Ask for a string
orig_string = input("Convert to Acronym : ")
 
# Convert the string to all uppercase
orig_string = orig_string.upper()
 
# Convert the string into a list
list_of_words = orig_string.split()
 
# Cycle through the list
for word in list_of_words:
 
    # Get the 1st letter of the word and eliminate the newline
    print(word[0], end="")
 
print()
 
# ---------- MORE STRING METHODS ---------- 
# very useful
 
letter_z = "z"
num_3 = "3"
a_space = " "
 
# Returns True if characters are letters or numbers
# Whitespace is false
print("Is z a letter or number :", letter_z.isalnum())
 
# Returns True if characters are letters
print("Is z a letter :", letter_z.isalpha())
 
# Returns True if characters are numbers (Floats are False)
print("Is 3 a number :", num_3.isdigit())
 
# Returns True if all are lowercase
print("Is z a lowercase :", letter_z.islower())
 
# Returns True if all are uppercase
print("Is z a uppercase :", letter_z.isupper())
 
# Returns True if all are spaces
print("Is space a space :", a_space.isspace())