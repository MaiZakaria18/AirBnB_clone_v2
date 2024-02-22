#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.amenity import Amenity

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place", cascade="delete")
    else:
        @property
        def reviews(self):
            """getter attribute the return reviews instances with place_id"""
            from models import storage
            Review = []
            review_list = storage.all("Reviews")
            for rev in review_list.values():
                if self.id == rev.place_id:
                    Review.append(rev)
            return Review

        @property
        def amenities(self):
            """getter attribute the return Amenity instances"""
            amenities = []
            amenities_list = models.storage.all("Amenity")
            for amenity in amenities_list.values():
                if self.id == amenity.place_id:
                    amenities.append(amenity)
            return amenities
        
        @amenities.setter
        def amenities(self, amenity=None):
            '''
            handles append method for adding an
            Amenity.id to the attribute amenity_ids
            '''
            if type(amenity) is Amenity and amenity.id not in self.amenity_ids:
                self.amenity_ids.append(amenity.id)
