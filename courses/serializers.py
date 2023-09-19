from rest_framework import serializers

from courses.models import Course


class CoursesSerializer(serializers.ModelSerializer):
    lesson_counter = serializers.IntegerField(source='lesson_set.all.count')

    class Meta:
        model = Course
        fields = ('id', 'title', 'image', 'description', 'lesson_counter')
