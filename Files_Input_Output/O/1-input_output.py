#!/usr/bin/python3

a_file = open('file1.py') #this opens file1 in the default read mode.Creating a new file(a_file)

read_file = a_file.read() #the read function is applied to a_file one , and the content show in read_file

print(read_file)  , print(a_file.read)

a_file.close() #file most be closed always after open to free up reasources and memory , to avoid issues

#to avoid the issue of always closing this is the right way to open a file for performing any operation on it:

with open('file1.py', "r", encoding="utf-8") as a_file: #opens the file1.py in the read mode,in a_file,and in unicode encoding format for binary tranlastion
    read_file = a_file.read()
    print(read_file)
    """This method ensures that the file will closee aytomatically no matter what"""

""" OTHER MODES USED TO OPERATE ON FILES WHEN OPENING
Mode	Description
r	    Open a file for reading. (default)
w	    Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	    Open a file for exclusive creation. If the file already exists, the operation fails.
a	    Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	    Open in text mode. (default)
b	    Open in binary mode.
+	    Open a file for updating (reading and writing)"""

