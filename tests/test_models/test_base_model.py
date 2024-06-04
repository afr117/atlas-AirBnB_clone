# tests/test_models/test_base_model.py
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if an instance of BaseModel is created correctly"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        """Test conversion of BaseModel instance to dictionary"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_save(self):
        """Test if the save method updates `updated_at` attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)


if __name__ == '__main__':
    unittest.main()

