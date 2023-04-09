#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as argument.
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state name searched>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    
    """In SQL, the BINARY keyword is used to perform a case-sensitive search when comparing strings. By default, most SQL databases perform case-insensitive searches when comparing strings,
meaning that "hello" and "HELLO" would be considered the same value. However, in some cases, it may be important to perform a case-sensitive search to distinguish between different values.
In the code snippet provided, the BINARY keyword is used to perform a case-sensitive search on the name column of the states table in the MySQL database. The BINARY keyword forces the 
database to compare the values of the name column using the binary representation of the string, rather than using a case-insensitive comparison.
For example, if the name column contains the values "Texas" and "texas", a case-insensitive search would consider these values to be the same and return both rows. 
However, if a case-sensitive search is performed using the BINARY keyword, only the row with the exact value "Texas" (matching capitalization) would be returned.
Note that the BINARY keyword is specific to MySQL and may not be supported by other SQL databases.
    """
    [print(state) for state in c.fetchall()]
