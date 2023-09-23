from django.conf import settings
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
    payed_price = models.IntegerField()

    payment_type = models.CharField(
        max_length=50,
        choices=PAYMENT_TYPES
    )

    def __str__(self):
        return f'{self.user} - {self.course if self.course else self.lesson}'

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
        ordering = ('-payment_date',)
