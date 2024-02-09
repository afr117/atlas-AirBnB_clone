#!/usr/bin/python3
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage = None

    def test_save_reload(self):
        # Create a BaseModel instance
        obj_id = "88cf87cf-830a-4715-acea-1417af600f53"
        my_model = BaseModel(id=obj_id, name="My_First_Model", my_number=89)
        
        # Save the object
        self.storage.new(my_model)
        self.storage.save()

        # Reload the data from the file
        self.storage.reload()

        # Check if the object is present in __objects dictionary
        self.assertIn(f"BaseModel.{obj_id}", self.storage.all())

        # Check the attributes of the reloaded object
        reloaded_obj = self.storage.all()[f"BaseModel.{obj_id}"]
        self.assertEqual(reloaded_obj.id, obj_id)
        self.assertEqual(reloaded_obj.name, "My_First_Model")
        self.assertEqual(reloaded_obj.my_number, 89)

if __name__ == '__main__':
    unittest.main()

