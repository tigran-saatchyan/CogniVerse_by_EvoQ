from rest_framework import serializers

from courses.models import Course
from lessons.serializers import LessonSerializer


class CoursesSerializer(serializers.ModelSerializer):
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
        fields = (
            'id',
            'title',
            'image',
            'description',
            'owner',
            'lessons',
            'lesson_counter'
        )
