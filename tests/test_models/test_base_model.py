#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init_with_kwargs(self):
        """Test initialization of the BaseModel with kwargs."""
        kwargs = {
                "id": "123",
                "created_at": "2023-01-01T12:00:00.000000",
                "updated_at": "2023-01-02T12:00:00.000000",
                "name": "Test Model",
                "value": 42
                }
        ob = BaseModel(**kwargs)

        self.assertEqual(ob.id, "123")
        self.assertEqual(ob.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(ob.updated_at, datetime(2023, 1, 2, 12, 0, 0))
        self.assertEqual(ob.name, "Test Model")
        self.assertEqual(ob.value, 42)

    def test_init_without_kwargs(self):
        """Test initialization of BaseModel without kwargs."""
        ob = BaseModel()

        self.assertIsInstance(ob.id, str)
        self.assertIsInstance(ob.created_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method."""
        ob = BaseModel()
        ob.name = "Test Model"
        ob.value = 42

        ob_dict = ob.to_dict()

        self.assertEqual(ob_dict['__class__'], 'BaseModel')
        self.assertEqual(ob_dict['name'], 'Test Model')
        self.assertEqual(ob_dict['value'], 42)

    def test_save(self):
        """Test the save method of BaseModel."""
        ob = BaseModel()
        created_at_before_save = ob.created_at
        ob.save()
        updated_at_after_save = ob.updated_at

        self.assertEqual(created_at_before_save, ob.created_at)
        self.assertGreater(updated_at_after_save, created_at_before_save)

    if __name__ == '__main__':
        unittest.main()
