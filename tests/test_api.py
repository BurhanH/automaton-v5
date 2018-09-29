import unittest
from calls import get_posts


class APITest(unittest.TestCase):
    """
    Test class to test API calls
    """
    def test_request_response(self):
        """
        Simple test
        """
        response = get_posts()

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
