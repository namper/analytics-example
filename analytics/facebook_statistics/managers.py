from django.db import models
from django.utils import timezone
from django.db.models import functions
from typing import Generic, TypeVar, TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from facebook_statistics.models import Post

_M = TypeVar('_M', bound=models.Model)


class QS(Generic[_M], models.QuerySet):
    """ Typing helper for queryset"""

    def __iter__(self) -> Iterable[_M]: ...


class PostQuerySet(models.QuerySet):

    def last_30_day_average(self, user_id: int) -> QS[dict]:
        # 0. get last 30 days posts
        delta_30 = timezone.now() - timezone.timedelta(days=30)
        post_from_lat_30_days = self.filter(user_id=user_id, created__gte=delta_30)
        # 1. annotate post creation day
        # 2. group by creation day
        # 4. annotate each day by average likes count
        return post_from_lat_30_days.annotate(
            day=functions.TruncDate('created')
        ).values('day').annotate(
            avg_likes=models.Avg('likes_count'))

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
