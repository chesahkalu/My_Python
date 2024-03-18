#!/usr/bin/python3

import os

"""this syntax is used to get the value of environment variables already set in the system"""

user = os.getenv('USER') # get the value of environment variable 'USER' which is already set in the system
print(user) # print the value of environment variable 'USER'

"""if the environment variable 'USER' is not set in the system, then the value of user will return None"""
user = os.getenv('USER' , 'No user') # this will return 'No user' if the environment variable 'USER' is not set in the system



user = os.environ['USER'] # this is another method of getting the value of environment variable 'USER', but this will raise an exception if the environment variable 'USER' is not set in the system
user = os.environ.get['USER'] # this will return None if the environment variable 'USER' is not set in the system.
print(user)


"""To set the value of environment variable 'USER' in the system, we can use the following syntax

On your terminal, type the following command: "export database=mysql" and press enter. This will create an
environment variable 'database' with value 'mysql' in the system if it doesn't already exist.

This environment variable will be available to all the programs running in the current shell. If you open a new
shell, the environment variable 'database' will not be available to the programs running in the new shell.
When you close the current shell, the environment variable 'database' will be deleted from the system."""


"""To set the value of environment variable 'USER' in the system permanently, we can use the following syntax

A .env file can be used to store the value of environment variables permanently in the system. The .env file
will be automatically loaded when the system starts up. The .env file should be placed in the home directory
of the user. The .env file should be in the following format: database=mysql ,  one environment variable per line."""

"""This file can be included inthe .gitignore file so that it is not pushed to the remote repository as it contains
private information. An .env.example file can be created which will contain the names of the environment variables"""


"""The python-dotenv package allows a Python application to import variables defined in a .env file into the environment. 
You can install python-dotenv in your virtual environment using pip:  pip install python-dotenv"""

from dotenv import load_dotenv
load_dotenv() #this will load the environment variables from the .env file into the environment. If a .env file is not found in the current directory, then the parent directory is searched for it./
#               you can also verify the path to the .env file to be searched - load_dotenv(path)

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')