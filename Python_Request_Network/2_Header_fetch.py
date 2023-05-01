#!/usr/bin/python3
import urllib.request


if __name__ == "__main__":

    request = urllib.request.Request("https://example.com")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        
        head = response.headers #gets header information of the response, which is a mapping object that maps header names to values.
        print(head)
        
        dict_head= dict(head) #converts the header info to a dictionary, which makes it easier to access the individual header values.
        
        
        print(dict_head)
        
        print(dict_head.get('Content-Length')) #gets the value of the Content-Length header using the get() method.
        
        with open("example.html", mode="wb") as html_file: #writes the body of the response to a file. wb is used to write in binary mode.
            html_file.write(body) #writes the body of the response to a file.
        