from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from facebook_statistics.models import Post
from facebook_statistics.serializer import PostSerializer


class PostViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
