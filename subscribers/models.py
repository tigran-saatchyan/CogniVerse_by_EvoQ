from datetime import datetime

from django.conf import settings
from django.db import models

from courses.models import Course


class Subscriber(models.Model):
    """
    Model representing a subscriber to a course.

    This model represents a user's subscription to a specific course. It
    includes fields for the user,
    the course they are subscribed to, and the date when the subscription
    was added.

    Attributes:
        user (User): The user who is subscribed to the course.
        course (Course): The course to which the user is subscribed.
        date_added (DateTimeField): The date and time when the subscription
        was created (auto-generated).

    Methods:
        __str__(): Returns a string representation of the subscriber,
        including the user and course.

    Usage:
        - Use this model to track user subscriptions to courses in your
        Django application.
    """

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
