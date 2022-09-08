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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
