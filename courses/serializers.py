from rest_framework import serializers

from courses.models import Course
from lessons.serializers import LessonSerializer
from lessons.validators import UrlValidator


class CoursesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model.

    This serializer is used to convert Course model instances to JSON format
    and vice versa.
    It includes fields for the course title, image URL, description, owner,
    lessons, lesson counter,
    and a boolean field indicating whether the current user is subscribed to
    the course.

    Fields:
        id (int): The unique identifier of the course.
        title (str): The title of the course.
        image (str): The URL of the course image.
        description (str): The description of the course.
        owner (int): The ID of the user who owns the course.
        lessons (list): A list of lesson objects serialized using
        LessonSerializer.
        lesson_counter (int): The total number of lessons in the course.
        is_subscribed (bool): Indicates whether the current user is
        subscribed to the course.

    Meta:
        model (Course): The Course model to be serialized.
        validators (list of UrlValidator): Validators to apply to the
        'description' field.

    Note:
        - The 'is_subscribed' field is read-only and is computed based on
        the relationship between users
          and courses.
        - The 'lessons' field is read-only and is populated using the
        'lesson_set' relationship on the Course model.
        - The 'lesson_counter' field is read-only and represents the total
        number of lessons associated with the course.

    Usage:
        - Use this serializer to serialize Course objects to JSON format for
        API responses.
        - When creating or updating courses, ensure that the 'description'
        field is validated using the UrlValidator.
    """

    is_subscribed = serializers.BooleanField(
        source='subscriber.all.exists',
        read_only=True
    )
    lessons = LessonSerializer(
        source='lesson_set',
        many=True,
        read_only=True
    )
    lesson_counter = serializers.IntegerField(
        source='lesson_set.all.count',
        read_only=True
    )

    class Meta:
        model = Course
        validators = [UrlValidator(field='description')]
        fields = (
            'id',
            'title',
            'image',
            'description',
            'owner',
            'lessons',
            'lesson_counter',
            'is_subscribed'
        )
