from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost


class WordPressAuto:
    def __init__(self):
        self.id = "owner"
        self.password = "n7dfvxi8"
        self.url = "https://kasoken-jo.com/debug/xmlrpc.php"
        self.which = "publish"
        self.wp = Client(self.url, self.id, self.password)

    def wp_auto_post(self, title, content, category: dict):
        post = WordPressPost()
        post.post_status = self.which
        post.title = title
        post.content = content
        post.terms_names = {
            "category": [category]
        }
        self.wp.call(NewPost(post))
