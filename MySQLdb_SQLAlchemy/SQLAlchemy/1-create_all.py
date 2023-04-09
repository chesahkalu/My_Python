#!/usr/bin/python3
#Creates table in DB if not created yet, for already defined City class- Look at model_cit1.py
#Remember, any module to create table for must be imported to establish the relationship between class and DB.

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_city1 import City #imported to establish relationship between class and DB
"""
Note that you don't need to import all model modules explicitly; 
importing the package itself (import models) is sufficient as long as the package's __init__.py file imports all the necessary modules.
Read more about configuring the __init__.py file here: https://docs.python.org/3/tutorial/modules.html#packages , to improt all the necessary modules.
"""

# Define engine and metadata objects
engine = create_engine('mysql+mysqldb://user:password@host/db_name') #engine object is created using create_engine() function for the MySQL database.
Base = declarative_base()
Base.metadata.bind = engine

# Create the cities table
Base.metadata.create_all()

# Verify that the table was created
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
results = session.query(City).all()
print(results)
session.close()

"""
In this example, we first import the necessary SQLAlchemy modules (create_engine, Column, Integer, String, ForeignKey, and declarative_base)
and the City class from the model_city module.
We then create an engine object using create_engine() connected to the MySQL database,
and bind it to the metadata of the declarative base class using Base.metadata.bind = engine.
Finally, we call Base.metadata.create_all() to create the table for the City class. 
We then verify that the table was created correctly by creating a session, querying for all City objects, and printing the results.

"""