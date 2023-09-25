from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from courses.models import Course
from courses.paginators import CoursesPaginator
from courses.serializers import CoursesSerializer
from users.permissions import IsOwnerOrManager


class CoursesViewSet(viewsets.ModelViewSet):
    pagination_class = CoursesPaginator
    serializer_class = CoursesSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsOwnerOrManager()]
        if self.action in ['list', 'retriv']:
            return [AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()

        course.owner = self.request.user
        course.save()
