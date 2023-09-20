from rest_framework import viewsets

from courses.models import Course
from courses.serializers import CoursesSerializer
from users.permissions import IsManager


class CoursesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsManager]

    serializer_class = CoursesSerializer
    queryset = Course.objects.all()
