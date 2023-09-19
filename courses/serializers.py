from rest_framework import serializers

from courses.models import Course
from lessons.serializers import LessonSerializer


class CoursesSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='lesson_set', many=True)
    lesson_counter = serializers.IntegerField(source='lesson_set.all.count')

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'image',
            'description',
            'lessons',
            'lesson_counter'
        )
