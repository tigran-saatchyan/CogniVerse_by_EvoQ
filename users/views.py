from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.permissions import IsOwnerOrReadOnly
from users.serializers import UserSerializer, UserRegistrationSerializer


class UserListView(generics.ListAPIView):
    """
    View for listing users.

    This view allows listing all users in the system. It provides read-only
    access to user data.

    Attributes:
        serializer_class (UserSerializer): The serializer used for user data.
        queryset (QuerySet): The query set to fetch all users.

    Usage:
        - Use this view to retrieve a list of users in your Django REST
        framework API.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRegistrationView(generics.CreateAPIView):
    """
    View for user registration.

    This view allows creating new user accounts. It is used for user
    registration and account creation.

    Attributes:
        serializer_class (UserRegistrationSerializer): The serializer used
        for user registration data.
        queryset (QuerySet): The query set to fetch all users.

    Usage:
        - Include this view in your API to enable user registration and
        account creation functionality.
    """
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UsersUpdateView(generics.UpdateAPIView):
    """
    View for updating user profiles.

    This view allows authenticated users to update their own user profiles.
    It enforces the
    'IsOwnerOrReadOnly' permission to ensure users can only update their own
    profiles.

    Attributes:
        permission_classes (list): The list of permission classes applied to
        this view.
        serializer_class (UserSerializer): The serializer used for user data.
        queryset (QuerySet): The query set to fetch all users.

    Usage:
        - Include this view in your API to allow users to update their own
        user profiles.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersRetrieveView(generics.RetrieveAPIView):
    """
    View for retrieving user profiles.

    This view allows retrieving user profiles by their unique identifier. It
    provides read-only access
    to user data.

    Attributes:
        serializer_class (UserSerializer): The serializer used for user data.
        queryset (QuerySet): The query set to fetch all users.

    Usage:
        - Use this view to retrieve user profiles by their unique identifier
        in your API.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersDestroyView(generics.DestroyAPIView):
    """
    View for deleting user accounts.

    This view allows authenticated users to delete their own user accounts.
    It enforces the
    'IsOwnerOrReadOnly' permission to ensure users can only delete their own
    accounts.

    Attributes:
        permission_classes (list): The list of permission classes applied to
        this view.
        serializer_class (UserSerializer): The serializer used for user data.
        queryset (QuerySet): The query set to fetch all users.

    Usage:
        - Include this view in your API to allow users to delete their own
        user accounts.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()
