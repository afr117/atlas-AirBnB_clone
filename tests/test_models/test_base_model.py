#!/usr/bin/python3
"""
This module contains the unit tests for the BaseModel class.
"""

import unittest
from datetime import datetime
import sys
sys.path.append('../')  # Add the parent directory to the Python path
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_attributes(self):
        """
        Test initialization of BaseModel attributes.
        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_method(self):
        """
        Test the save method of the BaseModel class.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel class.
        """
        model = BaseModel()
        self.assertIn("[BaseModel] ({})".format(model.id), str(model))

if __name__ == "__main__":
    unittest.main()

