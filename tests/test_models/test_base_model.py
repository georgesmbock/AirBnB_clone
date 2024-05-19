#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_generation(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        initial_updated_at = self.base_model.updated_at
        with patch('models.storage.new') as mock_new, \
             patch('models.storage.save') as mock_save:
            self.base_model.save()
            self.assertNotEqual(initial_updated_at,
                                self.base_model.updated_at)
            mock_new.assert_called_once_with(self.base_model)
            mock_save.assert_called_once()

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id,
                                                    self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    if __name__ == '__main__':
        unittest.main()
