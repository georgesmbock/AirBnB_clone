#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class that defines all the common 
    attribute/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        instantiates an object with its
        attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime
                                .strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns the string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of__dict__of the instance
        """
        instance_dict = {**self.__dict__}
        instance_dict['__class__'] = type(self).__name__
        instance_dict['created_at'] = instance_dict['created_at'].isoformat()
        instance_dict['updated_at'] = instance_dict['updated_at'].isoformat()

        return instance_dict
