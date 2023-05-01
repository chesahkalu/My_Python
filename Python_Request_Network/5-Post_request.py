#!/usr/bin/python3

import requests


"""The post() method sends a POST request to the specified URL. The json parameter is used to send a JSON object as a request. 
The json parameter can also be used to send a dictionary, which will be converted to a JSON object before sending. """



url = "https://jsonplaceholder.typicode.com/posts" # this url is a fake online REST API for testing and prototyping. Post requests sent to this URL will be saved as resources of type posts.
data = {"title": "foo", "body": "bar", "userId": 1} # this is the data that will be sent as a JSON object in the POST request.

r = requests.post(url, json=data) #sends a POST request to the URL and assigns the response to r.

print(r.status_code) #prints the status code of the response. 200 means OK. 201 means Created (the request has been fulfilled and resulted in a new resource being created).
print(r.json()) #prints the body of the response, which is a JSON object. json() is an attribute of the response object that returns the content of the response, in unicode.
print(r.text) #prints the body of the response, which is a string. text is an attribute of the response object that returns the content of the response, in unicode.
print(r.headers) #prints the header of the response. headers is an attribute of the response object that returns the header of the response, which is a mapping object that maps header names to values.