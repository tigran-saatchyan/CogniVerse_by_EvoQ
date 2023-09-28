from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from courses.models import Course
from courses.paginators import CoursesPaginator
from courses.serializers import CoursesSerializer
from users.permissions import IsOwnerOrManager


class CoursesViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing courses.

    This viewset provides CRUD operations (Create, Retrieve, Update, Partial
    Update, Delete) for courses.

    Attributes:
        pagination_class (CoursesPaginator): The pagination class to use for
        list views.
        serializer_class (CoursesSerializer): The serializer class for courses.
        queryset (QuerySet): The queryset for retrieving courses.

    Methods:
        list: List all courses.
        retrieve: Retrieve a single course by ID.
        create: Create a new course.
        update: Update a course by ID.
        partial_update: Partially update a course by ID.
        destroy: Delete a course by ID.
        get_permissions: Override to specify permissions for different actions.
        perform_create: Override to set the owner of the course upon creation.

    Permissions:
        - For 'create', 'update', 'partial_update', and 'destroy' actions,
        only the owner or a manager can access.
        - For 'list' and 'retrieve' actions, no authentication is required (
        AllowAny).
        - For other actions, standard DRF permissions apply (IsAuthenticated
        by default).

    """

    pagination_class = CoursesPaginator
    serializer_class = CoursesSerializer
    queryset = Course.objects.all()

    def list(self, request, *args, **kwargs):
        """
        List all courses.

        Returns:
            Response: A list of all courses serialized using CoursesSerializer.
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single course by ID.

        Returns:
            Response: A single course serialized using CoursesSerializer.
        """
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create a new course.

        Args:
            request (Request): The HTTP request object containing course data.

        Returns:
            Response: The newly created course serialized using
            CoursesSerializer.
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update a course by ID.

        Args:
            request (Request): The HTTP request object containing updated
            course data.

        Returns:
            Response: The updated course serialized using CoursesSerializer.
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a course by ID.

        Args:
            request (Request): The HTTP request object containing partial
            course data.

        Returns:
            Response: The partially updated course serialized using
            CoursesSerializer.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a course by ID.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: No content (HTTP 204) on successful deletion.
        """
        return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        """
        Return the permissions that should be used for the current action.

        Returns:
            list: A list of permission classes based on the current action.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsOwnerOrManager()]
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Create a new course instance and set the owner to the current user.

        Args:
            serializer (CoursesSerializer): The serializer instance used for
            course creation.

        Returns:
            None
        """
        course = serializer.save()
        course.owner = self.request.user
        course.save()
