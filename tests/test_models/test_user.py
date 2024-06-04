import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.user = User()

    def test_instance_creation(self):
        """Test if an instance of User is created correctly"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test if the User instance has the correct attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        """Test conversion of User instance to dictionary"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")

    def test_save(self):
        """Test if the save method updates `updated_at` attribute"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old_updated_at)


if __name__ == '__main__':
    unittest.main()
