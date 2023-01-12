#!/usr/bin/python3
#parts of strings can be picked up like arrays
word = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(word)
print(word[0])#first letter
print(word[4])#5th letter
print(word[5:])#6ths letter to end
print(word[:5])# first letter to 4th
print(word[:-1])#begining to 2nd to last letter, last is 0
print(word[5:-2])#5th to 3rd to last
print(f'{len(word)}')#gets the number of letters in
