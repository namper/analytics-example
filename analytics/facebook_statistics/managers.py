from django.db import models
from typing import Generic, TypeVar, TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from facebook_statistics.models import Post

_M = TypeVar('_M', bound=models.Model)


class QS(Generic[_M], models.QuerySet):
    """ Typing helper for queryset"""

    def __iter__(self) -> Iterable[_M]: ...


class PostQuerySet(models.QuerySet):

    def get_latest(self: QS['Post'], post_id: int) -> 'Post':
        """ get latest post by id"""
        return self.filter(post_id=post_id).latest()
