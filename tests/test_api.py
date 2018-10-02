import unittest
from calls import get_posts, get_comments

HTTP_OK = 200


class TestAPI(unittest.TestCase):
    """
    This tests some API calls
    """
    def test_get_posts(self):
        """
        Testing posts
        """
        response = get_posts()

        self.assertEqual(response.status_code, HTTP_OK)

    def test_get_post(self):
        """
        Testing post
        """
        response = get_posts(6)  # range 1 - 100

        self.assertEqual(response.status_code, HTTP_OK)

    def test_get_comments(self):
        """
        Testing comments
        """
        response = get_comments()

        self.assertEqual(response.status_code, HTTP_OK)

    def test_get_comment(self):
        """
        Testing comment
        """
        response = get_comments(120)  # range 1 - 500

        self.assertEqual(response.status_code, HTTP_OK)


if __name__ == "__main__":
    unittest.main()
