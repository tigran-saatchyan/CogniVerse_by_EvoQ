from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from sevice.constants import NULLABLE
from sevice.utils import save_picture
from users.managers import CustomUserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name='email', validators=[
            validators.EmailValidator(message="Invalid Email")
        ]
    )
    telephone = models.CharField(
        max_length=50,
        verbose_name='telephone',
        **NULLABLE
    )
    image = models.ImageField(
        upload_to=save_picture,
        verbose_name='avatar',
        **NULLABLE
    )
    country = models.CharField(
        max_length=50,
        verbose_name='country',
        **NULLABLE
    )
    city = models.CharField(
        max_length=50,
        verbose_name='city',
        **NULLABLE
    )
    is_verified: bool = models.BooleanField(
        verbose_name='is verified',
        default=False
    )
    date_added: datetime = models.DateTimeField(
        verbose_name='creation date',
        auto_now_add=True
    )
    date_modified: datetime = models.DateTimeField(
        verbose_name='date modified',
        auto_now=True
    )
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('date_added',)
