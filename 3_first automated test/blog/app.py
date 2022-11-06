from blog import Blog


MENU_PROMPT = '\nEnter "c" to create a blog, "l" to list them, "r" to read one, "p" to write a post, or "q" to quit: '
POST_TEMPLATE = """
--- {} ---

{}

"""

blogs = dict()


def show_menu():
    print_blogs()
    selection = input(MENU_PROMPT)



def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


if __name__ == '__main__':
    show_menu()
