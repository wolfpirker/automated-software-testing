from unittest import TestCase
from blog import Blog


class TestBlog(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

    def test_to_json_no_posts(self):
        b = Blog('Test Article', 'John Doe')
        expected = {
            'title': b.title,
            'author': b.author,
            'posts': []
        }
        self.assertDictEqual(expected, b.to_json())


    def test_to_json(self):
        b = Blog('Test Article', 'John Doe')
        b.create_post('Test Post', 'Test Content')
        expected = {
            'title': b.title,
            'author': b.author,
            'posts': [
                {
                    'title': 'Test Post',
                    'content': 'Test Content'
                }

            ]
        }
        self.assertDictEqual(expected, b.to_json())

