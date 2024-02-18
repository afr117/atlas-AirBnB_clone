import json

class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if exists)."""
        try:
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create instances based on class name
                    if class_name == 'User':
                        from models.user import User
                        obj = User(**value)
                    else:
                        from models.base_model import BaseModel
                        obj = BaseModel(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
