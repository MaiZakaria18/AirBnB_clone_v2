#!/usr/bin/python3
"""Defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """Getter attribute to retrieve cities associated with state"""
            cities = []
            citiesList = storage.all("City")  # Retrieve all City instances
            for city in citiesList.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
