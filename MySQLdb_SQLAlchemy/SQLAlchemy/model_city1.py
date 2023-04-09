#!/usr/bin/python3
# Defines a City model.
# Inherits from SQLAlchemy Base and links to the MySQL table cities.

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
"""
The base class created using the declarative_base function in SQLAlchemy serves as a parent class for all your ORM classes. 
It contains some metadata and functionality that is inherited by all the ORM classes defined using this base class.
The Base class created in the example code contains the following attributes and methods:
* metadata: A collection of table metadata that holds information about the database tables defined using this base class.
* query: A method that creates a new Query object for querying the database using this base class.
* __tablename__: An attribute that can be set in your ORM classes to specify the name of the corresponding database table.
* __mapper__: A method that returns the Mapper object used to map the class to the database table.
* __init__: A constructor method that initializes new instances of the class.
When you define an ORM class that inherits from this base class, the class inherits these attributes and methods, and 
you can use them to interact with the database. For example, you can define a new ORM class, set its __tablename__ attribute,
and use the query method to query the corresponding database table.
"""

class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (str): The city's id.
        name (sqlalchemy.Integer): The city's name.
        state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    """
    The City class defines a Python ORM class for interacting with a MySQL database table named "cities".
    The class inherits from the Base class, which was created using the declarative_base function from SQLAlchemy. 
    This means that the City class inherits some default behavior and metadata from the Base class, such as the __tablename__ attribute.
    The City class defines three attributes:
* id: An integer column that serves as the primary key for the cities table.
* name: A string column that holds the name of the city.
* state_id: An integer column that holds the foreign key to the id column of the states table.
    Each attribute is defined using the Column class, which is imported from the sqlalchemy module. 
    The Column class specifies the data type of the attribute, as well as any additional constraints, 
    such as whether the column can be null or whether it's a primary key.The __tablename__ attribute specifies 
    the name of the database table that corresponds to this ORM class. In this case, the table is named "cities".
    The ForeignKey function is also imported from the sqlalchemy module and is used to specify the foreign key constraint on the state_id column. 
    It specifies that the state_id column references the id column of the states table.
    
  *  The declarative metaclass provides a default constructor for model classes. 
    (e.g. __init__() method) which automatically accepts keyword names that match the columns we’ve mapped.
    e.g. city = City(name="San Francisco", state_id=1) 
    
  *  Assuming your table is already created in the database,
  The table columns must match the class attributes.If you change your declared classes, you need to explicitly alter the schema in the actual database too.
  
    """