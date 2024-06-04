import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_instance_creation(self):
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        self.assertEqual(self.state.name, "")

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')


if __name__ == '__main__':
    unittest.main()
