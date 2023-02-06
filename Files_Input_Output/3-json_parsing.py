#!/usr/bin/python3

"""
JSON (JavaScript Object Notation) is a popular data format used for representing structured data. 
It's common to transmit and receive data between a server and web application in JSON format. 
Code to parse, read and write JSON in Python. Also, converting JSON to dict and pretty print it."""

"""
normally in python json existas as string
also it can exist as a file, and to work and parse or print or convert from file to string, 
we import the json moule"""

import json

person = '{"name": "Bob", "languages": ["English", "French"]}' #json string
person_dict = json.loads(person) #this parses the string to return a dictionary
print( person_dict) #prints dictionary of person

with open('path_to_file/person.json', 'r') as f: #this opens a file containing json string(object)
  data = json.load(f) #this parses the file into a dictionary
print(data) #prints dictionary of person

"""note ~loads~ is used toparse the json string while ~load~ is used to parse the file"""

#this whole function can be done in the opposite direction>>>>>>

person_dict = {'name': 'Bob','age': 12,'children': None} #a dictionary
person_json = json.dumps(person_dict) #this turns it to a json string
print(person_json) #prints a json string


person_dict = {"name": "Bob", "languages": ["English", "French"], "married": True, "age": 32} # a dictionary

with open('person.txt', 'w') as json_file: #this opens a file in writing mode
  json.dump(person_dict, json_file) #this writes the dictionary into a file called son file in json string mode


