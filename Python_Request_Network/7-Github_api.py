#!/usr/bin/python3

import requests
import sys

username = str(sys.argv[1]) # get the username passed as argument to the script , ensure it is a string

url = "https://api.github.com/users/" + username # concatenate the username to the url , to get the default github api url for the user => https://api.github.com/users/username

r = requests.get(url) # send a GET request to the url and assign the response to r

json = r.json() # get the json representation of the response

print(json) # print the json representation of the response

print(json.get("name")) # print the value of the "name" key in the json representation of the response

for k, v in json.items():
    print("{}: {}".format(k, v)) # print the key and value of each item in the json representation of the response

"""Be careful: only 60 requests by hour by IP for unauthenticated requests - https://docs.github.com/en/rest"""