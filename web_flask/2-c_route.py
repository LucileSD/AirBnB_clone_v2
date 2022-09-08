#!/usr/bin/python3
"""
    starts a Flask web application
"""
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
