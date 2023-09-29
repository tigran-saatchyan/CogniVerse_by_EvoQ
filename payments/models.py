from django.conf import settings
from django.db import models

from courses.models import Course
from lessons.models import Lesson
from sevice.constants import NULLABLE
from users.models import User


class Payment(models.Model):
    """
    Model representing a payment.

    This model represents a payment made by a user for a course or a lesson.
    It includes fields for the user
    making the payment, payment date, associated course or lesson, payment
    amount, and payment type.

    Attributes:
        user (User): The user who made the payment.
        payment_date (DateTimeField): The date and time when the payment was
        made (auto-generated).
        course (Course): The course for which the payment was made (nullable).
        lesson (Lesson): The lesson for which the payment was made (nullable).
        paid_price (int): The amount paid for the course or lesson.
        payment_method (str): The type of payment, chosen from predefined
        choices.

    Methods:
        __str__(): Returns a string representation of the payment, including
        the user and associated course/lesson.

    Usage:
        - Use this model to represent payments made by users in your Django
        application.
    """

    PAYMENT_METHOD_CASH = 'cash'
    PAYMENT_METHOD_CARD = 'card'
    PAYMENT_METHOD_TRANSFER_TO_ACCOUNT = 'transfer_to_account'

    PAYMENT_METHODS = (
        (PAYMENT_METHOD_CASH, 'Cash'),
        (PAYMENT_METHOD_CARD, 'Card'),
        (PAYMENT_METHOD_TRANSFER_TO_ACCOUNT, 'Transfer to account'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="payment",
        on_delete=models.CASCADE,
        **NULLABLE
    )
    payment_date = models.DateTimeField(
        auto_now_add=True
    )
    course = models.ForeignKey(
        Course,
        related_name="payment",
        on_delete=models.CASCADE,
        **NULLABLE
    )
    lesson = models.ForeignKey(
        Lesson,
        related_name="payment",
        on_delete=models.CASCADE,
        **NULLABLE
    )
    paid_price = models.IntegerField()
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHODS,
        **NULLABLE
    )

    def __str__(self):
        return f'{self.user} - {self.course if self.course else self.lesson}'

    class Meta:
        unique_together = [["user", "course"], ["user", "lesson"]]
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
        ordering = ('-payment_date',)
