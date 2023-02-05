#!/usr/bin/python3

a_file = open('file1.py') #this opens file1 in the default read mode.Creating a new file(a_file)

read_file = a_file.read() #the read function is applied to a_file one , and the content show in read_file

print(read_file)  , print(a_file.read)

a_file.close() #file most be closed always after open to free up reasources and memory , to avoid issues