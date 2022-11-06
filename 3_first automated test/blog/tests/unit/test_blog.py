from unittest import TestCase
from blog import Blog

class TestBlog(TestCase):
    def test_create_blog(self):
        b = Blog('Test Article', 'John Doe')

        self.assertEqual('Test Article', b.title)
        self.assertEqual('John Doe', b.author)
        self.assertListEqual([], b.posts)
        # self.assertEqual(0, len(b.posts)) # this as alternative to the above

    def test__repr__(self):
        b = Blog('Test Article', 'John Doe')
        b2 = Blog('Test Article 2', 'Max')
        self.assertEqual(b.__repr__(), 'Test Article by John Doe (0 posts)')
        self.assertEqual(b2.__repr__(), 'Test Article 2 by Max (0 posts)')

    # Note: another test case we could implement
    # create multiple posts and check whether it appears correctly


