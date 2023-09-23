from rest_framework import serializers

from lessons.models import Lesson
from lessons.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'image', 'owner')
        validators = [UrlValidator(field='description')]
