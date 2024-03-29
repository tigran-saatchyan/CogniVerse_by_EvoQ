"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from lessons.apps import LessonsConfig
from lessons.views import (
    LessonCreateView, LessonListView, LessonRetrieveView, LessonUpdateView,
    LessonDestroyView
)

app_name = LessonsConfig.name

router = DefaultRouter()

urlpatterns = [
    path('create/', LessonCreateView.as_view(), name='lesson-create'),
    path('', LessonListView.as_view(), name='lesson-list'),
    path('<int:pk>', LessonRetrieveView.as_view(), name='lesson-retrieve'),
    path('update/<int:pk>', LessonUpdateView.as_view(), name='lesson-update'),
    path('destroy/<int:pk>', LessonDestroyView.as_view(), name='lesson-destroy'),
] + router.urls
