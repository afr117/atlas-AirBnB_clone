#!/usr/bin/python3
"""
This module defines the FileStorage class.
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """
    FileStorage class for serializing and deserializing objects to/from JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        try:
            # Create an empty dictionary to store JSON-serializable representations of objects
            json_dict = {}
        
            # Iterate over each key-value pair in __objects dictionary
            for key, value in self.__objects.items():
                # Convert the object to a dictionary representation using to_dict() method
                json_dict[key] = value.to_dict()
        
            # Open the JSON file in write mode
            with open(self.__file_path, 'w') as file:
                # Serialize the dictionary to JSON and write it to the file
                json.dump(json_dict, file)
        except Exception as e:
            print(f"Error saving objects: {e}")

    def reload(self):
        """
        Deserializes the JSON file to __objects (if file exists).
        """
        try:
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
        except Exception as e:
            print("ok")

