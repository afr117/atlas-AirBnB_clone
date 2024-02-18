#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""
import uuid
from datetime import datetime
class BaseModel:
    """
    BaseModel class for common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Call new method of storage to add the new object
            from models import storage
            storage.new(self)

    def save(self):
        """
@@ -44,7 +47,6 @@ def to_dict(self):
            obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


    def __str__(self):
        """
        Returns the string representation of the object.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
    def __repr__(self):
        """
        Returns the string representation of the object.
        """
        return str(self.to_dict())
