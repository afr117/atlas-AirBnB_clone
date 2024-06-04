import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        base_model = BaseModel()
        self.storage.new(base_model)
        key = base_model.__class__.__name__ + '.' + base_model.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        self.storage.reload()
        key = base_model.__class__.__name__ + '.' + base_model.id
        self.assertIn(key, self.storage.all())

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
