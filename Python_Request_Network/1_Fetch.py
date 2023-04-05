#!/usr/bin/python3
"""Fetches https://example.com"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://example.com")
    """
    The above code creates a request object for the URL. The URL can be passed directly to the below line.
    By creating a Request object, you can specify additional parameters for the request, such as headers
    data to be sent with the request, and HTTP method (GET, POST, PUT, etc.)
    """
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:") # 
        print("\t- type: {}".format(type(body))) #print the type of the body => bytes
        print("\t- content: {}".format(body)) #print the body, which is a bytes object indicated by b'...'
        print("\t- utf8 content: {}".format(body.decode("utf-8"))) #print the body decoded in utf-8, which is a string.
