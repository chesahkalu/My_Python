#!/usr/bin/python3

"""CSV files store datta in a tabular form, ending file name with (.csv) example below: 
SN, Name, City
1, Michael, New Jersey
2, Jack, California
...with each element seperated by a delimeter(any character), in our table above, a comma(,) is used which is default.
A similar function to files inputs and output in python is used to operate on CSV files, but a more
specific method is used to be able to control the rabular forms of the datas.
To use CSV files, import csv
"""

import csv


with open('people.csv', 'r') as file: #opens a file name "people.csv", in read mode.
    reader = csv.reader(file) #csv file read like this, and returns an object assigned to 'reader'. if delimeter = -, then(csv.read(file, delimeter='\t'))
    for row in reader: # reader looped throughrow by row and printed
        print(row)


"""to write csv file, a function first returns a string object in a tabular form with delimeter and the object can
tthen be written into a csv file"""

with open('protagonist.csv', 'w', newline='') as file: #file created and opened in a write mode
    writer = csv.writer(file) #write assigned the object
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])