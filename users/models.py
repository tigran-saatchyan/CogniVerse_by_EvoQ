from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from sevice.constants import NULLABLE
from sevice.utils import save_picture
from users.managers import CustomUserManager


class User(AbstractUser):
    """
    Custom user model that extends the AbstractUser model.

    This model represents a user with additional fields like email,
    telephone, image, country, and city.

    Attributes:
        email (EmailField): The email address of the user (unique).
        telephone (CharField): The telephone number of the user.
        image (ImageField): The user's avatar image.
        country (CharField): The user's country.
        city (CharField): The user's city.
        is_verified (BooleanField): Indicates whether the user's email is
        verified.
        date_added (DateTimeField): The date when the user account was created.
        date_modified (DateTimeField): The date when the user account was
        last modified.

    Methods:
        __str__(): Return a string representation of the user.

    Usage:
        - Use this custom user model as the base user model for your Django
        project.

    Example:
        ```python
        from django.contrib.auth.models import AbstractUser
        from django.db import models
        from users.managers import CustomUserManager

        class User(AbstractUser):
            email = models.EmailField(
                unique=True,
                verbose_name='email',
                validators=[validators.EmailValidator(message="Invalid Email")]
            )
            ...
        ```
    """

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
    last_login = models.DateTimeField(
        verbose_name='last login date',
        **NULLABLE
    )
    date_modified: datetime = models.DateTimeField(
        verbose_name='date modified',
        auto_now=True
    )
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        """
        Return a string representation of the user.

        Returns:
            str: The user's full name and email address.
        """
        return f'{self.first_name} {self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('date_added',)
