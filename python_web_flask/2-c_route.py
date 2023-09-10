#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False) #strict_slashes=False allows for both '/hbnb' and '/hbnb/' to return the same thing
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False) #the text variable passed in the URL is sent to the function as an argument
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ') # 'C' is printed followed by 'text' variable. Replace any underscore with a space 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
