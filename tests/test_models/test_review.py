import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_instance_creation(self):
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')


if __name__ == '__main__':
    unittest.main()
