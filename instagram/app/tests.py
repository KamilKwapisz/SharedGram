from django.test import Client, tag, TestCase
from django.urls import reverse

from .graph_models import Post, User, Photo


class CommentAddTestCase(TestCase):
    def setUp(self):
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')
        try:
            self.post = Post.nodes.get(name="post")
        except Post.DoesNotExist:
            pass
        else:
            self.post = Post(name="post", description="desc").save()
            self.author = User(name="tester").save()
            self.photo = Photo(name="photo").save()
            self.post.author.connect(self.author)
            self.post.photo.connect(self.photo)
            self.post.save()

    def test_adding_comment_with_proper_data(self):
        payload: dict = {
          "username": self.author.name,
          "text": "Test comment text",
          "post_uid": self.post.uid
        }
        response = self.client.post(reverse('api-comment-add'), payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.body['message'], "Success")


