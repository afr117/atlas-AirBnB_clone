import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_instance_creation(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        self.assertEqual(self.amenity.name, "")

    def test_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')


if __name__ == '__main__':
    unittest.main()
