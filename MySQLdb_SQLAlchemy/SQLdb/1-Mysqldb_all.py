#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    
    """This is a Python script that uses the MySQLdb library to connect to a MySQL database and retrieve the contents of a table named "states".
    The script takes three command-line arguments: the username, password, and database name.
    Here's a breakdown of what the code does:

* import MySQLdb: This line imports the MySQLdb library, which provides a Python interface to MySQL databases.
* from sys import argv: This line imports the argv variable from the sys module, which allows the script to access command-line arguments.
* if __name__ == "__main__":: This line is a standard Python idiom that ensures the following code only runs if the script is being executed as the main program, 
rather than being imported as a module into another script.
* db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8"): 
This line establishes a connection to the MySQL database using the connect() method of the MySQLdb library. 
The host and port arguments specify the location of the database (in this case, localhost and 3306, respectively). 
The user, passwd, and db arguments are read from the command-line arguments passed to the script. 
The charset argument specifies the character encoding used by the database.
* cursor = db.cursor(): This line creates a cursor object, which allows the script to interact with the database.
* cursor.execute("SELECT * FROM states ORDER BY id ASC"): This line executes a SQL query that selects all columns (*) from the states table 
and sorts the results by the id column in ascending order. 
* rows = cursor.fetchall(): This line retrieves all rows returned by the previous SQL query and stores them in the rows variable as a list of tuples.
The rows are stored in a list of tuples because the query returns multiple rows, and each row contains multiple columns.
* for row in rows: print(row): This line iterates over the rows returned by the query and prints each row(tuple) to the console.
* cursor.close(): This line closes the cursor object.
* db.close(): This line closes the database connection
    """