from django.db import models
from typing import Generic, TypeVar, TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from facebook_statistics.models import Post

_M = TypeVar('_M', bound=models.Model)


class QS(Generic[_M], models.QuerySet):
    """ Typing helper for queryset"""

    def __iter__(self) -> Iterable[_M]: ...


class PostQuerySet(models.QuerySet):

    def get_latest(self, post_id: int = None, user_id: int = None):
        assert (post_id or user_id) is not None
        if post_id:
            return self.get_latest_by_post(post_id)

        return self.get_latest_by_user(user_id)

    def get_latest_by_post(
            self: QS['Post'],
            post_id: int = None,
    ) -> 'Post':
        """ get latest post by id"""
        return self.filter(post_id=post_id).latest()

    def get_latest_by_user(self: QS['Post'], user_id: int):
        """ get latest Post statistics per user"""
        return self.filter(user_id=user_id).latest()
