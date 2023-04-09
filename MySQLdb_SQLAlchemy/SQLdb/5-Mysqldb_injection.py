#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as argument.
# Safe from SQL injections.
# Usage: ./3-my_safe_filter_states.py <mysql username> \
#                                     <mysql password> \
#                                     <database name> \
#                                     <state name searched>

"""SQL injection is a type of security vulnerability that can occur in applications that interact with a database. It happens when an attacker is able to inject SQL commands into an application's 
input fields or URL query parameters, which are then executed by the application's backend database.For example, let's say a website has a search function that allows users to search for products by name. 
The website's backend code might use SQL to query the database and return the search results. If the search function doesn't properly validate user input, an attacker could enter SQL code into the search 
box that modifies the database query to do something malicious. For example, where a search field for a product would complete an sql query to show the product like this; SELECT * FROM products WHERE name = 'red shoes';
the attacker could enter a search term like "red shoes; DROP TABLE products;" to delete the entire products table from the database. The sql query would then look like this; SELECT * FROM products WHERE name = 'red shoes'; DROP TABLE products;
The attacker could also enter a search term like "red shoes; UPDATE products SET price = 0;" to set the price of all products to $0.00.
 """
 
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
    
    
"""This code snippet is safe from SQL injection attacks since it does not use string formatting to insert user input into the SQL query. Instead, it only retrieves all rows from the states table using the SELECT * FROM states`` SQL statement, 
and then filters the results based on the value of sys.argv[4].The filtering is done in Python code using a list comprehension, which only prints out rows where the value of the second column (state[1]) matches the value of sys.argv[4]. 
Since the filtering is done in Python code and not in the SQL query, there is no risk of SQL injection attacks.
However, note that the code assumes that the sys.argv[4] value is safe to use without any further validation or sanitization. If sys.argv[4] is expected to be a specific data type (e.g. an integer or a date), 
it is recommended to validate and sanitize the input before using it in the code to prevent unexpected behavior or errors.
"""


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

"""This code uses a parameter placeholder %s in the query, and passes the user input as a parameter tuple to the execute() method. 
This ensures that the sys.argv[4] value is properly escaped and treated as data rather than executable code, making the query safe from SQL injection attacks.
"""
