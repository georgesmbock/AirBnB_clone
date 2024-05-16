#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """This class defines all common attributes/methods for other classes."""

    def __init__(self):
        """It's initializer of our class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """This method uppdates the public instance attribute updated_at
        with the current datetime.

        Args: None
        Return: None
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """This method returns a dictionary containing all keys/values
        of __dict__ of the instance.

        Args: None
        Returns: a dictionary
        """
        ob_dict = self.__dict__.copy()
        ob_dict['__class__'] = self.__class__.__name__
        ob_dict['created_at'] = self.created_at.isoformat()
        ob_dict['updated_at'] = self.updated_at.isoformat()
        return ob_dict

    def __str__(self):
        """This magic method prints:
        [<class name>] (<self.id>) <self.__dict__>

        Args: None
        Returns: The format
        """
        return f"[<{self.__class__.__name__}>] (<{self.id}>) <{self.__dict__}>"
