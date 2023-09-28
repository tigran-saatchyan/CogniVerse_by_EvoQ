from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="CogniVerse API",
        default_version='v1',
        description="API for CogniVerse Learning Management System",
        terms_of_service="https://github.com/tigran-saatchyan"
                         "/CogniVerse_by_EvoQ/blob/master/TERMS_OF_SERVICE",
        contact=openapi.Contact(
            email="mr.saatchyan@yandex.com",
            name="Tigran Saatchyan",
            url="https://github.com/tigran-saatchyan"
        ),
        license=openapi.License(
            name="MIT License",
            url="https://github.com/tigran-saatchyan/CogniVerse_by_EvoQ/blob"
                "/master/LICENSE"
        ),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        'swagger<format>/', schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
