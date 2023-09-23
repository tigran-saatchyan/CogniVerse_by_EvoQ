from rest_framework import generics

from users.models import User
from users.permissions import IsOwnerOrReadOnly
from users.serializers import (
    UserSerializer,
    UserRegistrationSerializer,
)


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UsersUpdateView(generics.UpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersDestroyView(generics.DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]

    serializer_class = UserSerializer
    queryset = User.objects.all()
