#!/usr/bin/python3
"""Takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
Eg: ./8-json_api.py <letter>
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1] # if no argument is passed, letter = "" else letter = sys.argv[1] (the argument passed) eg ./8-json_api.py a
    payload = {"q": letter} # payload is a dictionary with key "q" and value letter. The key "q" is the same as the key in the url http://

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload) # r is the response object
    try:
        response = r.json() # check if the response is a valid json
        if response == {}: # if the response is an empty dictionary
            print("No result") # print "No result"
        else: 
            print("[{}] {}".format(response.get("id"), response.get("name"))) # print the id and name of the response
    except ValueError:
        print("Not a valid JSON") # if the response is not a valid json, print "Not a valid JSON"

""" This script is designed to search for users based on a letter or partial name, and return the ID and name of the first matching user.
It is intended to be used with a web API that provides this functionality.

The 'q' key is used by the server to perform a search query, so this payload is telling the server what to search for. 
The search query is likely being performed on a user database, so 'q' could refer to a query for users whose names start with the specified letter, 
for example.

These keys and their values would need to be specified by the server API documentation or through communication with the server developers.
Depending on the requirements and capabilities of the server, there could be many other keys that can be included in the payload to perform various functions.
For example, there might be a 'limit' key that specifies the maximum number of search results to return, or an 'order' key that specifies the order in which 
the search results should be sorted."""
