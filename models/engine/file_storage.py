#!/usr/bin/python3
import json
from os import path
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """This class serializes intances to JSON file and
    deserializes JSON file to instances.
    She has two private class attributes:
    __file_pat: string - path to the JSON file (ex:file.jsonh)
    __objects: dictionary - empty but will store all objects
    by <class>.id
    (ex: to store a BaseModel object with id=12121212, the
    key will be BaseModel.12121212)
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """This method returns the dictionary __objects

        Args: None
        Return: Dictionary
        """
        return self.__objects

    def new(self, obj):
        """This method sets in _objects the obj with key
        <obj class name>.id

        Args:
        obj: Dictionary
        Return: None
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """This method serializes _objects to the
        JSON file (path: _file_path)

        Args: None
        Return: file
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'a') as f:
            json.dump(serialized_objects, f, indent=2)

    def reload(self):
        """This methods deserializes the JSON file
        to __objects (only if the JSON file (__file_path)
        exists; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)

        Args: None
        Return: None
        """
        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as json_file:
                    data = json.load(json_file)
                    for key, value in data.items():
                        class_name = value["__class__"]
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
            except json.JSONDecodeError:
                pass

    def delete(self, obj=None):
        """Deletes obj from _objects"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
                self.save()
