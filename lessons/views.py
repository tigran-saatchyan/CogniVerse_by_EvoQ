from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from lessons.models import Lesson
from lessons.paginators import LessonsPaginator
from lessons.serializers import LessonSerializer
from users.permissions import IsOwnerOrManager, IsPayed


class LessonCreateView(generics.CreateAPIView):
    permission_classes = [IsOwnerOrManager]

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def perform_create(self, serializer):
        lesson = serializer.save()

        lesson.owner = self.request.user
        lesson.save()


class LessonListView(generics.ListAPIView):
    permission_classes = [AllowAny]

    pagination_class = LessonsPaginator

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsPayed]

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(generics.UpdateAPIView):
    permission_classes = [IsOwnerOrManager]

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyView(generics.DestroyAPIView):
    permission_classes = [IsOwnerOrManager]

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
