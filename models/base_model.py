#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """This class defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """It's initializer of our class with *args and **kwargs.
        if kwarg is not empty:
        - each key this dictionary is an
        attribute name(Note __class from kwargs is the only one
        that should not be added as an attriibute.
        - each value of this dictionaryy is the value of this
        attribute name
        - Warning: created_at and updated_at are strings in this
        dictionary, but inside your Basemodel instance is
        working with datetime object. You have to convert these string into
        datetime object. Tip:you know the string format of these datetime.
        otherwise:
        - create id and created_at as you did previously(new instance).

        Args:
            *args: no used
            **kwargs: second argument
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    iso = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, iso))
                else:
                    setattr(self, key, value)
                self.id = str(uuid.uuid4())
        else:
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
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """This method returns a dictionary containing all keys/values
        of __dict__ of the instance.

        Args: None
        Returns: a dictionary
        """
        ob_dict =self.__dict__.copy()
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
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
