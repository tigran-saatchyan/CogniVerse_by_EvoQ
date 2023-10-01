from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import AllowAny

from courses.models import Course
from lessons.models import Lesson
from lessons.paginators import LessonsPaginator
from lessons.serializers import LessonSerializer, LessonCreateUpdateSerializer
from users.permissions import IsOwnerOrManager, IsPayed


class LessonCreateView(generics.CreateAPIView):
    """
    Create a new lesson.

    This view allows authenticated users who are owners or managers to
    create a new lesson.
    Lessons can be associated with courses or other educational content.

    Permissions:
        - Users must be authenticated to create a lesson (IsAuthenticated).
        - Only owners or managers can create lessons (IsOwnerOrManager).

    Request:
        - HTTP method: POST
        - Data: Lesson data in the request body serialized using
        LessonSerializer.

    Response:
        - HTTP status: 201 Created on successful creation.
        - Data: The newly created lesson serialized using LessonSerializer.

    Usage:
        - Use this view to create new lessons associated with courses or
        other educational content.
    """

    permission_classes = [IsOwnerOrManager]
    serializer_class = LessonCreateUpdateSerializer
    queryset = Lesson.objects.all()

    def perform_create(self, serializer):
        lesson = serializer.save()

        lesson.owner = self.request.user
        lesson.save()


class LessonListView(generics.ListAPIView):
    """
    List all lessons.

    This view allows any user, including unauthenticated users, to retrieve
    a list of all lessons.
    Lessons are paginated using the LessonsPaginator.

    Permissions:
        - No authentication is required to list lessons (AllowAny).

    Request:
        - HTTP method: GET

    Response:
        - HTTP status: 200 OK
        - Data: A paginated list of lessons serialized using LessonSerializer.

    Usage:
        - Use this view to retrieve a list of all lessons for public or
        authorized access.
    """

    permission_classes = [AllowAny]
    pagination_class = LessonsPaginator
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all().order_by('id')


class LessonRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve a lesson by ID.

    This view allows authenticated users who have paid for access to
    retrieve a lesson by its ID.
    Lessons can be associated with courses or other educational content.

    Permissions:
        - Users must be authenticated to retrieve a lesson (IsAuthenticated).
        - Users must have paid for access to retrieve a lesson (IsPayed).

    Request:
        - HTTP method: GET
        - URL parameter: 'pk' - The ID of the lesson to retrieve.

    Response:
        - HTTP status: 200 OK on successful retrieval.
        - Data: The retrieved lesson serialized using LessonSerializer.

    Usage:
        - Use this view to retrieve individual lessons for authorized users.
    """

    permission_classes = [IsPayed]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(generics.UpdateAPIView):
    """
    Update a lesson by ID.

    This view allows authenticated users who are owners or managers to
    update a lesson by its ID.
    Lessons can be associated with courses or other educational content.

    Permissions:
        - Users must be authenticated to update a lesson (IsAuthenticated).
        - Only owners or managers can update lessons (IsOwnerOrManager).

    Request:
        - HTTP method: PUT or PATCH
        - URL parameter: 'pk' - The ID of the lesson to update.
        - Data: Lesson data in the request body serialized using
        LessonSerializer.

    Response:
        - HTTP status: 200 OK on successful update.
        - Data: The updated lesson serialized using LessonSerializer.

    Usage:
        - Use this view to update existing lessons by their ID for
        authorized users.
    """

    permission_classes = [IsOwnerOrManager]
    serializer_class = LessonCreateUpdateSerializer
    queryset = Lesson.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        course = Course.objects.filter(pk=instance.course.pk)

        course.update(
            date_modified=timezone.now()
        )
        return super().update(request, *args, **kwargs)


class LessonDestroyView(generics.DestroyAPIView):
    """
    Delete a lesson by ID.

    This view allows authenticated users who are owners or managers to
    delete a lesson by its ID.
    Lessons can be associated with courses or other educational content.

    Permissions:
        - Users must be authenticated to delete a lesson (IsAuthenticated).
        - Only owners or managers can delete lessons (IsOwnerOrManager).

    Request:
        - HTTP method: DELETE
        - URL parameter: 'pk' - The ID of the lesson to delete.

    Response:
        - HTTP status: 204 No Content on successful deletion.

    Usage:
        - Use this view to delete lessons by their ID for authorized users.
    """

    permission_classes = [IsOwnerOrManager]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
