import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_instance_creation(self):
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')


if __name__ == '__main__':
    unittest.main()
