#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
- uses the GitHub API to display your id.
Eg: ./10-my_github.py <GitHub username> <GitHub password>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

    """This is a Python script that uses the requests library to make an authenticated GET request to the GitHub API 
    to retrieve the user information for the authenticated user.
    
    The script takes two command-line arguments: the username and password/token for the GitHub account.
    
    These arguments are used to create an HTTPBasicAuth object, which is then passed to the auth parameter of 
    the requests.get() function to authenticate the request.
    
    The response from the API is then printed to the console as JSON, and the user ID is extracted from the JSON using 
    the get() method and printed to the console as well."""
