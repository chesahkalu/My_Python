#!/usr/bin/python3
"""Fetches https://example.com body content"""


import sys
import requests


if __name__ == "__main__":
    r = requests.get("https://example.com") #sends a GET request to the URL and assigns the response to r.
    print("Body response:")
    print("\t- type: {}".format(type(r.text))) #print the type of the body => str
    print("\t- content: {}".format(r.text)) #print the body, which is a string. text is an attribute of the response object that returns the content of the response, in unicode.
