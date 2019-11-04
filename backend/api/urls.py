from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'university', UniversityViewSet, basename='university')

urlpatterns = [
    # documentation views
    path('docs/',
         TemplateView.as_view(template_name='swagger-ui.html',
                              extra_context={'schema_url': 'openapi-schema'}),
         name='docs'),
    path('redocs/',
         TemplateView.as_view(template_name='redoc.html',
                              extra_context={'schema_url': 'openapi-schema'}),
         name='redocs'),

    # OpenAPI schema
    path('openapi/',
         get_schema_view(
             title="Portal API",
             description="Portal API Schema",
         ),
         name='openapi-schema'),

    # all API ends
    *router.urls
]
