#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_rep(self):
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        created_at = self.model.created_at
        self.model.save()
        self.assertNotEqual(created_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(model_dict.keys(), expected_keys)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(datetime.fromisoformat(model_dict
                                                     ['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat
                              (model_dict['updated_at']), datetime)

    if __name__ == '__main__':
        unittest.main()
