from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"{self.title} by {self.author} ({len(self.posts)} posts)"

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def to_json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.to_json() for post in self.posts],
        }
