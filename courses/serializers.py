from rest_framework import serializers

from courses.models import Course
from lessons.serializers import LessonSerializer
from lessons.validators import UrlValidator


class CoursesSerializer(serializers.ModelSerializer):
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
