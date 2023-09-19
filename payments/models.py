from django.db import models

from courses.models import Course
from lessons.models import Lesson
from sevice.constants import NULLABLE
from users.models import User


class Payment(models.Model):

    PAYMENT_TYPE_CASH = 'cash'
    PAYMENT_TYPE_TRANSFER_TO_ACCOUNT = 'transfer_to_account'

    PAYMENT_TYPES = (
        (PAYMENT_TYPE_CASH, 'Cash'),
        (PAYMENT_TYPE_TRANSFER_TO_ACCOUNT, 'Transfer to account'),
    )

    user = models.ForeignKey(
        User,
        related_name="payment",
        on_delete=models.CASCADE,
        **NULLABLE
    )
    payment_date = models.DateTimeField(
        auto_now_add=True
    )
    course_bought = models.ForeignKey(
        Course,
        related_name="payment",
        on_delete=models.CASCADE,
        **NULLABLE
    )
    lesson_bought = models.ForeignKey(
        Lesson,
        related_name="payment",
        on_delete=models.CASCADE,
        **NULLABLE
    )
    payed_price = models.IntegerField()

    payment_type = models.CharField(
        max_length=50,
        choices=PAYMENT_TYPES
    )
