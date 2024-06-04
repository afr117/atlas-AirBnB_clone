import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                created_at_str = kwargs['created_at']
                self.created_at = datetime.strptime(
                    created_at_str, "%Y-%m-%dT%H:%M:%S.%f"
                )
            if 'updated_at' in kwargs:
                updated_at_str = kwargs['updated_at']
                self.updated_at = datetime.strptime(
                    updated_at_str, "%Y-%m-%dT%H:%M:%S.%f"
                )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
        # Add code to save to file storage

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

