from django.conf import settings
from django.db import models
from courses.models import Course
from sevice.constants import NULLABLE
from sevice.utils import save_picture
from users.models import User


class Lesson(models.Model):
    """
    Model representing a lesson.

    This model represents an individual lesson within a course. It includes
    fields for the lesson's title,
    description, associated course, preview image, owner, and timestamps for
    creation and modification.

    Attributes:
        title (str): The title of the lesson (up to 150 characters).
        description (str): The description of the lesson (textual content).
        course (Course): The course to which the lesson belongs.
        image (ImageField): The preview image associated with the lesson.
        owner (User): The user who owns or created the lesson.
        date_added (DateTimeField): The date and time when the lesson was
        added (auto-generated).
        date_modified (DateTimeField): The date and time when the lesson was
        last modified (auto-updated).

    Methods:
        __str__(): Returns a string representation of the lesson, which is
        its title.

    Usage:
        - Use this model to represent individual lessons in a course within
        your Django application.
    """

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
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="lesson",
        on_delete=models.CASCADE,
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
