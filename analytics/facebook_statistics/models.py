from django.db import models
from django.utils.translation import gettext_lazy as _
from facebook_statistics import managers


class Post(models.Model):
    post_id = models.PositiveBigIntegerField(verbose_name=_('Post id'), db_index=True)
    user_id = models.PositiveBigIntegerField(verbose_name=_('User id'), db_index=True)
    likes_count = models.PositiveIntegerField(verbose_name=_('Likes count'))

    created = models.DateTimeField(auto_now_add=True)

    objects = managers.PostQuerySet.as_manager()

    def __str__(self):
        return f'Post {self.post_id} by {self.user_id}'

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        get_latest_by = ('created',)
