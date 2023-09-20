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
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import (
    UserRegistrationView,
    UserListView,
    UsersUpdateView,
    UsersRetrieveView,
)

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
    path('create/', UserRegistrationView.as_view(), name='users-create'),
    path('<int:pk>/', UsersRetrieveView.as_view(), name='user-retrieve'),
    path('update/<int:pk>', UsersUpdateView.as_view(), name='users-update'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
