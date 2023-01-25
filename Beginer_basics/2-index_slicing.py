#!/usr/bin/python3
#parts of strings can be picked up like arrays
word = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(word)
print('word is a ', type(word), ' type')#type function can be used to find the data type of any data,
print(word[2:9])#When we slice lists, the first figure goes for the value at the index, the start index is inclusive but the end index is exclusive.
print(word[:1])
print(word[:0])#empty space is printed
print(word[0])#first letter
print(word[4])#5th letter
print(word[5:])#6th letter to end
print(word[:5])# first letter to 4th index
print(word[:-1])#begining to 2nd to last letter, last is 0
print(word[5:-2])#5th index to 3rd to last
print(f'{len(word)}')#gets the number of letters in word

word_c = word + ' ' + 'a' + 'b' + 'c' #this is called concatenating, and is possible with various datatypes and structures.
print(word_c)

num=('123456789')

word_num = '' #creates an empty string,some other data structures and types can be created like this empty

for i in word:
    word_num = word_num + i

for c in num:
    word_num += c

print(word_num)
