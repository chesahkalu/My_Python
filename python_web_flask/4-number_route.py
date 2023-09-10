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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False) #maps to the URL path /number/<int:n>, where <n> is a variable part of the URL that must be an integer
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n) # If 'n' is not an integer, it will return a 404 error

"""Overall, this route can be used to ensure that a value provided in the URL is an integer before processing it further. 
This can be useful in scenarios where integer values are expected, such as when working with database IDs or other numerical data."""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
