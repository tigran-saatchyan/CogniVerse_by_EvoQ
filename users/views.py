from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer, UserRegistrationSerializer


class UserListSerializer(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UsersUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
