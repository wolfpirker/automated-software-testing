from unittest import TestCase
from post import Post

class TestPost(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test content', p.content)

    def test_to_json(self):
        p = Post('Test', 'Test content')
        expected = {'title': p.title, 'content': p.content}
        self.assertDictEqual(expected, p.to_json())


