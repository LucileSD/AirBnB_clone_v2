#!/usr/bin/python3
"""
    starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ just say hello"""
    message = "Hello HBNB!"
    return message


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ say hbnb"""
    message = "HBNB"
    return message


@app.route("/c/<text>", strict_slashes=False)
def CIsFun(text):
    """ take the value of a variable"""
    newText = text.replace("_", " ")
    message = "C " + newText
    return message


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonIs(text="is cool"):
    """ take the value of a variable"""
    newText = text.replace("_", " ")
    message = "Python " + newText
    return message


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """ display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberTemplate(n):
    """ display a HTML page only if n is an integer"""
    return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
