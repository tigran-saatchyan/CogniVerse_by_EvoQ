from django.db import models

from courses.models import Course
from sevice.constants import NULLABLE
from sevice.utils import save_picture


class Lesson(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='title'
    )
    description = models.TextField(
        verbose_name='description',
        **NULLABLE
    )
    course = models.ForeignKey(
        Course,
        verbose_name='course',
        on_delete=models.CASCADE,
        **NULLABLE
    )
    image = models.ImageField(
        upload_to=save_picture,
        verbose_name='preview image',
        **NULLABLE
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='date added'
    )
    date_modified = models.DateTimeField(
        auto_now=True,
        verbose_name='date modified'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
