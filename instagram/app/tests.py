from django.test import Client, tag, TestCase
from django.urls import reverse

from rest_framework import status

from .graph_models import Post, User, Photo


class CommentAddTestCase(TestCase):

    def setUp(self):
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')
        self.POST_NAME = "POST_FOR_TESTS"
        self.AUTHOR_NAME = "AUTHOR_TESTER"
        self.PHOTO_NAME = "PHOTO_FOR_TESTS"
        try:
            self.post = Post.nodes.get(name=self.POST_NAME)
        except Post.DoesNotExist:
            self.post = Post(name=self.POST_NAME, description="desc1").save()
            self.author = User(name=self.AUTHOR_NAME).save()
            self.photo = Photo(name=self.PHOTO_NAME).save()
            self.post.author.connect(self.author)
            self.post.photo.connect(self.photo)
            self.post.save()
        else:
            self.author = User.nodes.get(name=self.AUTHOR_NAME)
            self.photo = Photo.nodes.get(name=self.PHOTO_NAME)

    @tag('fast')
    def test_adding_comment_with_proper_data(self):
        payload: dict = {
          "username": self.author.name,
          "text": "Test comment text",
          "post_uid": self.post.uid
        }
        response = self.client.post(reverse('api-comment-add'), payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Success")

    @tag('fast')
    def test_adding_comment_with_invalid_post_uid(self):
        payload: dict = {
            "username": self.author.name,
            "text": "Test comment text",
            "post_uid": "This is definitely not a valid post uid"
        }
        response = self.client.post(reverse('api-comment-add'), payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['message'], "Post with this uid doesn't exist")

    @tag('fast')
    def test_adding_comment_with_invalid_username(self):
        payload: dict = {
            "username": "404",
            "text": "Test comment text",
            "post_uid": self.post.uid
        }
        response = self.client.post(reverse('api-comment-add'), payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['message'], "User with this username doesn't exist")
