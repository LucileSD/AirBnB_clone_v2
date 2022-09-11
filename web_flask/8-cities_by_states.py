#!/usr/bin/python3
"""
    starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def removeSql(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def listCity():
    """list cities in a state"""
    list = storage.all(State).values()
    return render_template("8-cities_by_states.html", list=list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
