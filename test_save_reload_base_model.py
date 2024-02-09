#!/usr/bin/python3
"""
Test script to demonstrate saving and reloading objects using BaseModel and FileStorage.
"""

from models import storage
from models.base_model import BaseModel

# Reload objects from the file, if any
print("-- Reloaded objects --")
for obj in storage.all().values():
    print(obj)

# Create a new object
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

