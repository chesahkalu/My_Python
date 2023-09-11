#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__) # creates an instance of the Flask class called "app", this allows Flask to find the location of the application's resources, such as templates and static files.


@app.route('/', strict_slashes=False) # strict_slashes=False allows for both '/hbnb' and '/hbnb/' to return the same thing
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug = True) #specify the url and port, without this it will run on "http://127.0.0.1:5000/""

# The method should be restarted manually for any change in the code. To overcome this, the debug support is enabled so as to track any error.
# on terminal enter = 'export FLASK_APP=0-hello_route.py' to set the file to be run as the flask app
# on terminal enter = 'flask run' to run the flask app
# or enter = 'python3 <filename>' to run the file directly
# The method should be restarted manually for any change in the code. To overcome this, the debug support is enabled so as to track any error.

