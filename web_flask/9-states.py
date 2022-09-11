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
    """  remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def listState():
    """list states in html page"""
    list = storage.all(State).values()
    return render_template("7-states_list.html", list=list)


@app.route("/states/<id>", strict_slashes=False)
def listStateId(id):
    """list states in html page"""
    list = storage.all(State).values()
    listState = []
    for element in list:
        if (element.id == id):
            listState.append(element)
            return render_template("9-states.html", list=listState,
                                   state=element, flag=1)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
