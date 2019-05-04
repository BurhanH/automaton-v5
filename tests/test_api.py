import unittest
from calls import get_posts, get_comments

HTTP_OK = 200                                       # Expect response code
POSTS = 100                                         # Expect quantity of posts
POST_ID = 6                                         # Expect post id
POST_TITLE = 'dolorem eum magni eos aperiam quia'   # Expect post title
COMMENTS = 500                                      # Expect quantity of comments
COMMENT_ID = 120                                    # Expect comment id


class TestAPI(unittest.TestCase):
    """
    This tests some API calls
    """
    def test_get_posts(self) -> None:
        """
        Testing posts
        """
        response = get_posts()
        self.assertEqual(response.status_code, HTTP_OK)

        data = response.json()
        self.assertEqual(len(data), POSTS, 'Getting less than {} posts!'.format(POSTS))

    def test_get_post(self) -> None:
        """
        Testing post
        """
        response = get_posts(POST_ID)
        self.assertEqual(response.status_code, HTTP_OK)

        data = response.json()
        self.assertEqual(data['id'], POST_ID, 'Expecting {}, instead getting {}!'.format(POST_ID, data['id']))

        self.assertTrue(
            data['title'] == POST_TITLE, 'Expecting {} title, getting {} title!'.format(POST_TITLE, data['title'])
        )

    def test_get_comments(self) -> None:
        """
        Testing comments
        """
        response = get_comments()
        self.assertEqual(response.status_code, HTTP_OK)

        data = response.json()
        self.assertEqual(len(data), COMMENTS, 'Getting less than {} posts!'.format(COMMENTS))

    def test_get_comment(self) -> None:
        """
        Testing comment
        """
        response = get_comments(COMMENT_ID)
        self.assertEqual(response.status_code, HTTP_OK)

        data = response.json()
        self.assertEqual(data['id'], COMMENT_ID, 'Expecting {}, instead getting {}!'.format(COMMENT_ID, data['id']))


if __name__ == "__main__":
    unittest.main()
