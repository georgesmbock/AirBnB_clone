#!/usr/bin/python3
"""The FileStorage script"""
import json
import os
from models.base_model import BaseModel
"""class that serializes instance to a JSON file and deserializes JSON file"""


class FileStorage:
    """string-path to the JSON file"""
    __file_path = 'file.json'
    """dictionary that stores all objects by class name"""
    __objects = {}

    def __init__(self):
        """Initialize the FileStorage instance."""
        self.__objects = {}

    def all(self):
        """returns the dictionary objects."""
        return self.__objects.copy()

    def new(self, obj):
        """set in obj with key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        my_objects = {}
        for key, obj in self.__objects.items():
            my_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(my_objects, file)

    def reload(self):
        """Deserializes the JSON file without raising exception"""
        from models.base_model import BaseModel
        """Import here to avoid circular import"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                """reset the __objects dict"""
                self.__objects.clear()
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = BaseModel(**obj_dict)
