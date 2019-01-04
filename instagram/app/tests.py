import uu
import uuid

from django.test import Client, tag, TestCase
from django.urls import reverse

from rest_framework import status

from .graph_models import Comment, Post, User, Photo


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
        # Given
        payload: dict = {
          "username": self.author.name,
          "text": "Test comment text",
          "post_uid": self.post.uid
        }

        # When
        response = self.client.post(reverse('api-comment-add'), payload)

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Success")

    @tag('fast')
    def test_adding_comment_with_invalid_post_uid(self):
        # Given
        payload: dict = {
            "username": self.author.name,
            "text": "Test comment text",
            "post_uid": "This is definitely not a valid post uid"
        }

        # When
        response = self.client.post(reverse('api-comment-add'), payload)

        # Then
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['message'], "Post with this uid doesn't exist")

    @tag('fast')
    def test_adding_comment_with_invalid_username(self):
        # Given
        payload: dict = {
            "username": "404",
            "text": "Test comment text",
            "post_uid": self.post.uid
        }

        # When
        response = self.client.post(reverse('api-comment-add'), payload)

        # Then
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['message'], "User with this username doesn't exist")

    @tag('fast')
    def test_adding_comment_without_obligatory_key(self):
        # Given
        payload: dict = {
            "text": "Test comment text",
            "post_uid": self.post.uid
        }

        # When
        response = self.client.post(reverse('api-comment-add'), payload)
        missing_key = "username"

        # Then
        self.assertEqual(response.status_code, status.HTTP_402_PAYMENT_REQUIRED)
        self.assertEqual(response.data['message'], f"Invalid request. No '{missing_key}' key in request")


class PostCreateTestCase(TestCase):

    def setUp(self):
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')
        self.PHOTO_NAME = "PHOTO_FOR_TESTS"
        self.AUTHOR_NAME = "AUTHOR_TESTER"
        self.RANDOM_POST_NAME = uuid.uuid4()
        try:
            self.photo = Photo.nodes.get(name=self.PHOTO_NAME)
        except Photo.DoesNotExist:
            self.photo = Photo(name=self.PHOTO_NAME).save()
            self.author = User(name=self.AUTHOR_NAME).save()
        else:
            self.author = User.nodes.get(name=self.AUTHOR_NAME)

    @tag('fast')
    def test_creating_post_with_proper_data(self):
        # Given
        description = "Testing description"
        payload: dict = {
            "username": self.author.name,
            "name": self.RANDOM_POST_NAME,
            "description": description,
            "photo_uid": self.photo.uid,
        }

        # When
        response = self.client.post(reverse('api-post-create'), payload)
        created_post = Post.nodes.get(name=self.RANDOM_POST_NAME)

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Success")
        self.assertEqual(created_post.author.single().name, self.author.name)
        self.assertEqual(created_post.description, description)
        # self.assertEqual(created_post.photo.single().name, self.photo.name) # TODO photos

    @tag('fast')
    def test_creating_post_with_invalid_username(self):
        # Given
        payload: dict = {
            "username": "Wrong_username",
            "name": self.RANDOM_POST_NAME,
            "description": "Testing description",
            "photo_uid": self.photo.uid,
        }

        # When
        response = self.client.post(reverse('api-post-create'), payload)

        # Then
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['message'], "User with this username doesn't exist")

    # @tag('fast')
    # def test_creating_post_with_invalid_photo_uid(self):
    #     # Given
    #     payload: dict = {
    #         "username": self.author.name,
    #         "name": self.RANDOM_POST_NAME,
    #         "description": "Testing description",
    #         "photo_uid": "DEFINITELY_NOT_VALID_UID",
    #     }
    #
    #     # When
    #     response = self.client.post(reverse('api-post-create'), payload)
    #
    #     # Then
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #     self.assertEqual(response.data['message'], "Photo with this uid doesn't exist")

    @tag('fast')
    def test_creating_post_without_obligatory_key(self):
        # Given
        payload: dict = {
            "username": self.author.name,
            "name": self.RANDOM_POST_NAME,
            "photo_uid": self.photo.uid,
        }

        # When
        response = self.client.post(reverse('api-post-create'), payload)
        missing_key = "description"

        # Then
        self.assertEqual(response.status_code, status.HTTP_402_PAYMENT_REQUIRED)
        self.assertEqual(response.data['message'], f"Invalid request. No '{missing_key}' key in request")
