"""
URL configuration for the employee_management project.

This module defines the URL patterns for the project. For more information, please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.i18n import i18n_patterns

# Schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management API",
        default_version='v1',
        description="API documentation for the Employee Management app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL patterns for the admin site and Swagger documentation
urlpatterns = [
    path('admin/', admin.site.urls),  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI for API documentation
    path('swagger<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # Swagger JSON/YAML
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc for API documentation
]

# Internationalization (i18n) patterns
urlpatterns += i18n_patterns(
    path('', include('core.urls')),  # Include core app URLs
    path('i18n/', include('django.conf.urls.i18n')),  # Internationalization URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
    
)
