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
        with patch('builtins.input') as mocked_input:
            app.show_menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:
                app.show_menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

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