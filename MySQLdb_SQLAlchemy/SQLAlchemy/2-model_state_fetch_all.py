#!/usr/bin/python3
# Lists all State objects from the database hbtn_0e_6_usa.
# Usage: ./7-model_state_fetch_all.py <mysql username> /
#                                     <mysql password> /
#                                     <database name>

"""
After declaring class with with attributes as columns of a table in a database,
we can then connect to the data base, query the data base, and print the results using SQLAlchemy's ORM functionality.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))


"""
* The sys module is imported to allow the script to receive command-line arguments.
* The create_engine function from the sqlalchemy module is used to create a new database engine. 
The engine connects to a MySQL database using the credentials passed as command-line arguments (sys.argv[1], sys.argv[2], sys.argv[3]). 
The pool_pre_ping parameter is set to True to enable the "pre-ping" feature, which pings the server before each transaction to check if the connection is still valid.
* The sessionmaker function from the sqlalchemy.orm module is used to create a session class that will be used to interact with the database.
* The bind parameter is set to the previously created engine.
* An instance of the session class is created by calling the session class with no arguments.
* A for loop is used to query the State ORM class and retrieve all the states from the database. 
* The order_by method is used to sort the results by the id column.
* For each state retrieved from the database, the script prints the state's id and name attributes.
Overall, this code demonstrates a basic use case for SQLAlchemy's ORM functionality, 
by connecting to a database, querying data using ORM classes, and displaying the results.
"""

"""
Session: a container of instances of mapped classes; among other things lets you construct queries dynamically and add/delete/update entities.
REMEMBER: Session is a temporary connection to the database. It is used to query the database and add/delete/update entities.
READ MORE: https://docs.sqlalchemy.org/en/13/orm/session_basics.html
"""