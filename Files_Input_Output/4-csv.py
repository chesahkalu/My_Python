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

"""to read a csv file with non default deimiter, the delimeter must be indicated"""

with open('people.csv', 'r') as file: #opens a file name "people.csv", in read mode.
    reader = csv.reader(file) #csv file read like this, and returns an object assigned to 'reader'. 
                              #if delimeter = \, then "csv.read(file, delimeter='\t')"
                              #if there are space after csv file, then "csv.reader(csvfile, skipinitialspace=True)" , to remove space in read csv output
                              #if file has qutoe on parameter and quotes to be removed then "csv.reader(file, quoting=csv.QUOTE_ALL)"
    for row in reader: # reader looped throughrow by row and printed
        print(row)


"""to write csv file, a function first returns a string object in a tabular form with delimeter and the object can
then be written into a csv file"""

with open('protagonist.csv', 'w', newline='') as file: #file created and opened in a write mode
    writer = csv.writer(file) #writer assigned the object that would be written
    writer.writerow(["SN", "Movie", "Protagonist"]) #rows are written accordinly
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])


"""A two dimensional list can be written into a csv file, each list index taking a row number accordinly"""

csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]
with open('protagonist.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)
    
"""writing a csv file with a non default delimeter would be done like this"""

with open('protagonist.csv', 'w') as file:
    writer = csv.writer(file, delimiter = '\t')
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])

"""to read csv file as a dictionary for each row, with first row as key"""

with open("people.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row)) #the dict() method used to create dictionaries inside the for loop.

"""to write dictionaries into csv files"""

with open('players.csv', 'w', newline='') as file:
    fieldnames = ['player_name', 'fide_rating']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})
