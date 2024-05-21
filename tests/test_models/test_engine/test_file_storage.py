#!/usr/bin/python3
"""Module for testing file storage."""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_file.json'
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage._FileStorage__objects.clear()

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        """create new stroage instance for reload"""
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, new_storage.all())

    def test_reload_notexist_file(self):
        """Testing reload when file doesn't exist."""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
