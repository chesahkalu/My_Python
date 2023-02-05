#!/usr/bin/python3

a_file = open('file1.py') #this opens file1 in the default read mode.Creating a new file(a_file). you can specify the file directory infront

content = a_file.read() #the read function is applied to a_file one , and the content read into content

print(content)  , print(a_file.read)

a_file.close() #file most be closed always after open to free up reasources and memory , to avoid issues

#to avoid the issue of always closing this is the right way to open a file for performing any operation on it:

with open('file1.py', "r", encoding="utf-8") as a_file: #opens the file1.py in the read mode,in a_file,and in unicode encoding format for binary tranlastion
    content= a_file.read(10) #10 reads only the first 10 characters of the file, and if read again the first 10 wont be included
    print(content)
    """This method ensures that the file will closee automatically no matter what"""

""" OTHER MODES USED TO OPERATE ON FILES WHEN OPENING
Mode	Description
r	    Open a file for reading. (default)
w	    Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	    Open a file for exclusive creation. If the file already exists, the operation fails.
a	    Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	    Open in text mode. (default)
b	    Open in binary mode.
+	    Open a file for updating (reading and writing)"""


with open('test2.txt', 'w') as file2: #a file is open in write mode, nonexistence of file causes a creation of file,
    file2.write('Python is Fun.') #this goes to first line, and also everything in the file is deleted to start this
    file2.write('Python is cool') #second line
    file2.wirite('I love python\nI love it alot') #3rd lin, newline, 4th line

