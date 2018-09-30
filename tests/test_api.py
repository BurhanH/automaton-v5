import unittest
from calls import get_posts, get_comments
import random


class APITest(unittest.TestCase):
    """
    This tests some API calls
    """
    def test_get_posts(self):
        """
        Testing posts
        """
        response = get_posts()

        self.assertEqual(response.status_code, 200)

    def test_get_post(self):
        """
        Testing post
        """
        response = get_posts(random.randint(1, 100))

        self.assertEqual(response.status_code, 200)

    def test_get_comments(self):
        """
        Testing comments
        """
        response = get_comments()

        self.assertEqual(response.status_code, 200)

    def test_get_comment(self):
        """
        Testing comment
        """
        response = get_comments(random.randint(1, 500))

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
