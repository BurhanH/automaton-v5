import requests

POSTS_URL = 'http://jsonplaceholder.typicode.com/posts'


def get_posts():
    """
    Function to get posts
    """
    response = requests.get(POSTS_URL)

    if response.ok:
        return response
    return None
