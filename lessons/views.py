from rest_framework import generics

from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from users.permissions import IsManager


class LessonCreateView(generics.CreateAPIView):
    permission_classes = [IsManager]

    serializer_class = LessonSerializer


class LessonListView(generics.ListAPIView):
    permission_classes = [IsManager]

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsManager]

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(generics.UpdateAPIView):
    permission_classes = [IsManager]

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyView(generics.DestroyAPIView):
    permission_classes = [IsManager]

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
