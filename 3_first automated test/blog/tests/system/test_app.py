from unittest import TestCase
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

    def test_menu_prints_blogs(self):
        with patch('builtins.print') as mocked_print:
            # Note: if we don't give a input, we have to give the input
            # while testing (it will not finish the test itself!)
            with patch('builtins.input', return_value='q'):
                app.show_menu()

                mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.show_menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:
                mocked_input.side_effect = ('l', 'q')
                app.show_menu()
                mocked_print_blogs.assert_called()

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test 2', 'Test Author 2', 'y')
            app.ask_create_blog()
            # Note: following assertion does not result equal
            # surely because it is not the same object reference!
            # self.assertEqual(app.blogs['Test 2'], 'Test 2 by Test Author 2 (0 posts)')

            # so check whether fields are equal instead!
            self.assertIsNotNone(app.blogs.get('Test 2')) # rather not forget that!
            self.assertEqual((app.blogs['Test 2'].title), 'Test 2')
            self.assertEqual((app.blogs['Test 2'].author), 'Test Author 2')

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(app.blogs['Test'])

            # initial mistake in own attempt:
            # Note: patching builtins.print would be awkward;
            # better patch app.print_posts!
            # with patch('builtins.print') as mocked_print:
                # wrong! it is not about printing a single post
                # in this test we should call app.ask_read_blog()!
                # app.print_post(app.blogs['Test'])
                # mocked_print.assert_called_with(app.blogs['Test'])




    def test_ask_create_post(self):
        # app.ask_create_post() -> not here, but after our side effects!
        blog = app.blogs['Test']
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Post Title', 'Test Content')
            app.ask_create_post()
            self.assertEqual(blog.posts[0].title, 'Post Title')
            self.assertEqual(blog.posts[0].content, 'Test Content')


    def test_print_post(self):
        post = Post('Post title', 'Post content')
        # Note:
        # better it would be actually to not rely on POST_TEMPLATE
        # probably better to copy and paste the TEMPLATE here
        # when it is messed up in app.py, this test case would actually fail!
        # !!!

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(app.POST_TEMPLATE.format('Post title', 'Post content'))