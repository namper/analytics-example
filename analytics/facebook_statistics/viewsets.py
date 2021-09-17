from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from facebook_statistics.models import Post
from facebook_statistics.serializer import PostSerializer
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from rest_framework import status
from django.http import Http404


class PostViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=('get',), detail=True)
    def get_latest_by_post_id(self, _request: Request, **__) -> Response:
        latest_post: Post = self.get_latest('post_id')
        serializer = self.get_serializer(latest_post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=('get',), detail=True)
    def get_latest_by_user_id(self, _request: Request, **__) -> Response:
        latest_post: Post = self.get_latest('user_id')
        serializer = self.get_serializer(latest_post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=('get',), detail=True)
    def get_average_statistics(self, _request: Request, pk: int):
        average = self.get_queryset().last_30_day_average(user_id=pk)
        print(average)
        if not average:
            raise Http404
        return Response(data=average.values('date', 'avg_likes'))

    def get_latest(self, lookup: str):
        """ Returns the latest post object or raises 404 error """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {lookup: self.kwargs[lookup_url_kwarg]}
        try:
            obj = queryset.get_latest(**filter_kwargs)
        except queryset.model.DoesNotExist:
            raise Http404

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
