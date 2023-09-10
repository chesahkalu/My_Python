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

"""bellow, The route is decorated with two @app.route decorators, which means that the same 
    function will handle requests to both paths. The first route, /python, does not include a variable
    part of the URL, while the second route, /python/<text>, includes a variable part of the URL called <text>.
    
    For example, if a user visits the URL /python/rocks, Flask will call the pythoniscool() function with text 
    equal to "rocks". The function will then return the string "Python rocks", which will be sent as the HTTP 
    response to the user's browser.

    If a user visits the URL /python, Flask will call the pythoniscool() function with text equal to the default 
    value of "is cool". The function will then return the string "Python is cool", which will be sent as the HTTP 
    response to the user's browser.
"""
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
