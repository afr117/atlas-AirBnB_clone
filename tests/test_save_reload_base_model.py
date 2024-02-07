#!/usr/bin/python3
"""
Test module for BaseModel class.
"""
import os
import sys
import unittest

# Append the parent directory of the current file to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.base_model import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.model = BaseModel()
        self.model.name = "My_First_Model"
        self.model.my_number = 89

    def tearDown(self):
        """
        Clean up test environment.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage.reload()

    def test_save_method(self):
        """
        Test the save method of the BaseModel class.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel class.
        """
        self.assertIn("[BaseModel] ({})".format(self.model.id), str(self.model))

    def test_reload_method(self):
        """
        Test the reload method of the storage engine.
        """
        all_objs = storage.all()
        self.assertTrue(len(all_objs) > 0)

if __name__ == "__main__":
    unittest.main()

