#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             nullable=False, primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             nullable=False, primary_key=True)
                      )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id', ondelete="CASCADE"), 
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete", passive_deletes=True)
    amenities = relationship("Amenity", viewonly=False, secondary=place_amenity, back_populates='place_amenities')


    @property
    def reviews(self):
        """returns the list of Review"""
        new_list = []
        all_review = models.storage.all(Review)
        for element in all_review.values():
            if self.id == element.place_id:
                new_list.append(element)
        return new_list

        
    @property
    def amenities(self):
        """returns the list of amenities
        """
        new_list = []
        all_ami = models.storage.all(Amenity)
        for element in all_ami.values():
            if self.id == element.amenity_ids:
                new_list.append(element)
        return new_list
        
    @amenities.setter
    def amenities(self, val):
        if type(val) == "Amenity":
            self.amenity_ids.append(val.id)
