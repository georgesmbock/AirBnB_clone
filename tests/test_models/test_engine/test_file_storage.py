#!/usr/bin/python3
"""Module for testing file storage."""
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

        """Create a BaseModel instance for testing."""
        self.base_model = BaseModel()
        self.base_model.name = "Test_Model"
        self.base_model.my_number = 42

    def tearDown(self):
        """Test tear down environment.
        Remove the test BaseModel instance."""
        del self.base_model

        """Remove the test file after each test."""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_new(self):
        """Test the new model."""
        self.storage.new(self.base_model)

        """check if BaseModel is correctly added."""
        self.assertIn("BaseModel." + self.base_model.id,
                      self.storage._FileStorage__objects)

    def test_save(self):
        """Test the save method."""
        self.storage.new(self.base_model)
        self.storage.save()

        """check if the JSONN file is created."""
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Test the reload method."""
        self.storage.new(self.base_model)

        """save the objects to the JSON file."""
        self.storage.save()

        """reload the objects from JSON file."""
        self.storage.reload()

        """check if the objects was successfully reloaded"""
        self.assertIn("BaseModel." + self.base_model.id,
                      self.storage._FileStorage__objects)

    def test_delete(self):
        """Testing to delete an object from storage."""
        self.storage.new(self.base_model)

        """save the objects to the JSON file."""
        self.storage.save()

        """Delete the BaseModel instance from storage."""
        self.storage.delete(self.base_model)

        """check if the object exists before deletion."""
        self.assertNotIn("BaseModel." + self.base_model.id,
                         self.storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
