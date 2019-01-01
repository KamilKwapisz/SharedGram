from django.test import Client, tag, TestCase

from .graph_models import Post, User, Photo


class CommentAddTestCase(TestCase):
    def setUp(self):
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')
        self.post = Post(name="post", description="desc").save()
        self.author = User(name="tester").save()
        self.photo = Photo(name="photo").save()
        self.post.author.connect(self.author)
        self.post.photo.connect(self.photo)
        self.post.save()

    


