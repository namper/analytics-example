from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    post_id = models.PositiveBigIntegerField(verbose_name=_('Post id'), db_index=True)
    user_id = models.PositiveBigIntegerField(verbose_name=_('User id'))
    likes_count = models.PositiveIntegerField(verbose_name=_('Likes count'))

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-created', ]
