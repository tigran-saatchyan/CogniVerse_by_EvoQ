from django.conf import settings
from django.db import models

from sevice.constants import NULLABLE
from sevice.utils import save_picture


class Course(models.Model):
    """
    Model representing a course.

    This model stores information about a course, including its title,
    preview image, description,
    owner (related to the user who created the course), date added, and date
    modified.

    Fields:
        title (str): The title of the course (maximum length: 255 characters).
        image (ImageField): The preview image of the course, uploaded using
        the 'save_picture' function.
        description (str): The description of the course.
        owner (User): The user who owns the course, related to the
        settings.AUTH_USER_MODEL.
        date_added (datetime): The date and time when the course was added (
        auto-generated on creation).
        date_modified (datetime): The date and time when the course was last
        modified (auto-updated).

    Methods:
        __str__(): Returns the title of the course as its string
        representation.

    Meta:
        verbose_name (str): The human-readable name for a single course (
        singular).
        verbose_name_plural (str): The human-readable name for multiple
        courses (plural).

    Note:
        - The 'image' and 'description' fields are nullable, allowing for
        courses without images or descriptions.
        - The 'owner' field establishes a foreign key relationship with the
        user who created the course.
        - The 'date_added' field is automatically set to the current date
        and time upon creation.
        - The 'date_modified' field is automatically updated whenever the
        course is modified.

    Usage:
        - Use this model to represent courses in your application, storing
        relevant information.
    """

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
