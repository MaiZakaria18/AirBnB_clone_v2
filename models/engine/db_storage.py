
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
class DBStorage():
    __engine = None
    __session = None

    def __init__(self, *arg):
        mysql_user = os.environ.get("HBNB_MYSQL_USER")
        mysql_password = os.environ.get("HBNB_MYSQL_PWD")
        mysql_host = os.environ.get("HBNB_MYSQL_HOST", "localhost")
        mysql_db = os.environ.get("HBNB_MYSQL_DB")

        # Construct database URL
        dbURL = f"mysql+mysqldb://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"

        # Create database engine with connection pooling and pre-ping
        self.__engine = create_engine(dbURL, pool_pre_ping=True)

        # Drop tables if environment is set to test
        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Query objects from the database session"""

        # Define a list of classes to query if cls is None
        all_classes = [User, State, City, Amenity, Place, Review]

        # Query objects based on the specified class name or all classes
        if cls is None:
            objects = []
            for class_ in all_classes:
                objects.extend(self.__session.query(class_).all())
        else:
            objects = self.__session.query(cls).all()

        # Construct dictionary with class name and object ID as key
        object_dict = {}
        for obj in objects:
            key = f"{obj.__class__.__name__}.{obj.id}"
            object_dict[key] = obj

        return object_dict

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database schema and create a new session"""
        # Create all tables in the database
        Base.metadata.create_all(self.__engine)

        # Create a sessionmaker with specified options
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)

        # Create a scoped session to ensure thread safety
        self.__session = scoped_session(session_factory)
