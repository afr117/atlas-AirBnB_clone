#!/usr/bin/python3
"""
This module defines the FileStorage class.
"""
import json
from os import path
from models.base_model import BaseModel

class FileStorage:
    """
@@ -39,10 +39,12 @@ def reload(self):
        """
        Deserializes the JSON file to __objects (if file exists).
        """
        if path.exists(self.__file_path):
        try:
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
