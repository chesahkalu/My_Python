#!/usr/bin/python3
"""Displays X-Request-Id in the response header of a request to a given URL.
Eg: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1] #gets the URL passed as argument to the script.

    r = requests.get(url) #sends a GET request to the URL and assigns the response to r.
    print(r.headers.get("Expires"))  # gets header information of the response, which is a mapping object that maps header names to values. Then gets the value of the Expires header using the get() method.
