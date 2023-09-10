#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False) # maps to the URL path /number_template/<n>, where <n> is a variable part of the URL that must be an integer
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n) # render_template() function is used to render a template. It takes the template filename as the first argument, and a variable list of template arguments(like n=n)

"""The render_template() function is a Flask function that takes a template file and a set of variables and renders the template with those variables.
In this case, it is being used to render a template called 5-number.html,which should be located in the templates directory of the Flask application. 
The n variable is passed into the template and can be accessed within the template using the syntax {{ n }}.

The render_template() function can be used to create dynamic HTML pages that include variables that are passed in as arguments. This can be useful for 
displaying data from a database or other external source in a user-friendly way. The use of templates allows developers to separate the HTML markup from 
the application logic, making it easier to maintain and update the application over time."""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
