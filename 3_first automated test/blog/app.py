from blog import Blog

MENU_PROMPT = '\nEnter "c" to create a blog, "l" to list them, "r" to read one, "p" to write a post, or "q" to quit: '
POST_TEMPLATE = """
--- {} ---

{}

"""

blogs = dict()


def show_menu():
    # show the user the available blogs
    # let the user make a choice
    # exit on request
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def ask_create_blog():
    """ function to create basic blog entries"""
    # Note: this function ended up quite a bit complex;
    # course teacher suggestion: start simple and create a working test;
    # then extend gradually , and test in between
    title = str(input("enter a title as blog title: \n"))
    if (len(title)) <= 3:
        print('blog title must contain more than 3 letters')
        return
    author = str(input("enter an author or keep blank: \n"))
    b = Blog(title, author)
    # Note: instead just create blog without posts!
    # while True:
    #     # let user create several blog posts
    #     print('create a new post')
    #     title_pos = input("enter the post title (or leave blank to skip): \n")
    #     if len(title_pos) <= 3:
    #         print('skip')
    #         break
    #     else:
    #         content = input("enter the content: \n")
    #         b.create_post(title, content)
    answer = input("save blog y/n (y): ")
    if answer != 'n':
        blogs[b.title] = b
        print('blog created')
    else:
        print('blog entry canceled')


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def ask_read_blog():
    title = input("Enter the blog title you want to read:\n")
    # Note: try/catch not required, we keep it simplistic
    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    """basic function to create a single post for a blog"""
    blog = input("Enter the blog title you want to create a post in: ")
    b = blogs[blog]
    title = input("enter the post title (or leave blank to cancel): \n")
    if len(title) <= 3:
        print('cancel create post')
    else:
        content = input("enter the content: \n")
        b.create_post(title, content)


if __name__ == '__main__':
    show_menu()
