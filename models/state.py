#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """   
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref= "state", cascade="all, delete",
                          passive_deletes= True)
    @property
    def cities(self):
        """returns the list of City instances"""
        new_list = []
        all_cities = models.storage.all(City)
        for element in all_cities.values():
            if self.id == element.state_id:
                new_list.append(element)
        return new_list
