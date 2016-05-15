# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class OpenID(models.Model):
    user_email = models.EmailField(unique=True)
    time = models.TimeField()

    def __unicode__(self):
        return self.user_email

    class Meta:
        verbose_name = u'用户的邮箱'
        verbose_name_plural = u'用户的邮箱'

