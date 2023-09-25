from datetime import datetime

from django.conf import settings
from django.core import validators
from django.db import models

from courses.models import Course


class Subscriber(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscriber'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subscriber"
    )
    date_added: datetime = models.DateTimeField(
        verbose_name='creation date',
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'subscriber'
        verbose_name_plural = 'subscribers'
        unique_together = ["user", "course"]
