#!/usr/bin/python3
import uuid
from datetime import datetime
"""A class basemodel that defines all common attributes for other classes."""


class BaseModel:
    def __init__(self):
        """Defines initialization of instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """A string that prints class name, id and __dict__"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
        """returns the string of the attributes."""

    def save(self):
        """updates the public instance attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
