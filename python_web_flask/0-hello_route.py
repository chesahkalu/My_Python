#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__) # creates an instance of the Flask class called "app", this allows Flask to find the location and root path of the application's resources, such as templates and static files.
# __name__ is the name of the current Python module. The app needs to know where it's located to set up some paths, and __name__ is a convenient way to tell it that.
# you can also use the specific name of the file, but using __name__ is better because it's more reliable and just points to whatever module is currently being used as the entry point (so it won't break if you change the file name).
# The app variable is an instance of Flask, so you can use it like any other Python object. The Flask class has a constructor that takes the name of the current module (__name__) as argument.


@app.route('/', strict_slashes=False) # strict_slashes=False allows for both '/hbnb' and '/hbnb/' to return the same thing
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__': # if the script is executed directly, the code block is executed, if the script is imported, the code block is not executed.
    app.run(host='0.0.0.0', port='5000', debug = True) #specify the url and port, without this it will run on "http://127.0.0.1:5000/""

# The method should be restarted manually for any change in the code. To overcome this, the debug support is enabled so as to track any error.
# on terminal enter = 'export FLASK_APP=0-hello_route.py' to set the file to be run as the flask app
# on terminal enter = 'flask run' to run the flask app
# or enter = 'python3 <filename>' to run the file directly
# The method should be restarted manually for any change in the code. To overcome this, the debug support is enabled so as to track any error.

