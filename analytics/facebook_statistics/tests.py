from django.test import TestCase
from facebook_statistics.factory import PostFactory
from facebook_statistics.models import Post
from django.utils import timezone
from unittest.mock import patch
from datetime import datetime


class TestPostManager(TestCase):

    def test_get_latest_by_user(self):
        PostFactory.create_batch(size=3, user_id=1)
        last_post = PostFactory(user_id=1)
        result_latest_post = Post.objects.get_latest_by_user(user_id=1)
        self.assertEqual(last_post, result_latest_post)

    def test_get_latest_by_post(self):
        PostFactory.create_batch(size=3, post_id=4)
        last_post = PostFactory(post_id=4)
        result_latest_post = Post.objects.get_latest_by_post(post_id=4)
        self.assertEqual(last_post, result_latest_post)
