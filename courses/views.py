from django.shortcuts import render
from rest_framework import viewsets

from courses.models import Course
from courses.serializers import CoursesSerializer


# Create your views here.

class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Course.objects.all()
