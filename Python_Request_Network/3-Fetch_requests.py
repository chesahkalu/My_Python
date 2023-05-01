#!/usr/bin/python3
"""Fetches https://example.com body content"""


import sys
import requests


if __name__ == "__main__":
    r = requests.get("https://example.com") #sends a GET request to the URL and assigns the response to r.
    print (r.status_code) #prints the status code of the response. 200 means OK. 404 means Not Found. 403 means Forbidden. 500 means Internal Server Error. 503 means Service Unavailable. 504 means Gateway Timeout. 
    print (r.encoding) #prints the encoding of the response. UTF-8 means Unicode Transformation Format 8-bit. ISO-8859-1 means Latin Alphabet No. 1.
    print("Body response:")
    print("\t- type: {}".format(type(r.text))) #print the type of the body => str
    print("\t- content: {}".format(r.text)) #print the body, which is a string. text is an attribute of the response object that returns the content of the response, in unicode.
