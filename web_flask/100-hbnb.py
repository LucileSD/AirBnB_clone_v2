#!/usr/bin/python3
"""
    starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def removeSql(exception):
    """  remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display a HTML page HBNB"""
    listState = storage.all(State).values()
    listAmenity = storage.all(Amenity).values()
    listPlace = storage.all(Place).values()
    return render_template("100-hbnb.html", listState=listState,
                           listAmenity=listAmenity, listPlace=listPlace)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
