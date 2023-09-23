from django.conf import settings
from django.db import models

from sevice.constants import NULLABLE
from sevice.utils import save_picture


class Course(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="title"
    )
    image = models.ImageField(
        upload_to=save_picture,
        verbose_name="preview image",
        **NULLABLE
    )
    description = models.TextField(
        verbose_name="description",
        **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="course",
        on_delete=models.CASCADE,
        **NULLABLE
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date added"
    )
    date_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="date modified"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"
