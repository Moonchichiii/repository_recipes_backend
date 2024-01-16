from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('likes/', include('likes.urls')),
    path('followers/', include('followers.urls')),
    
    path('api/followers/', include('followers.urls')),
    
    path('api/', include(router.urls)),      
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
    
    path('docs/', include_docs_urls(title='API Documentation', public=True, permission_classes=[permissions.AllowAny])),
    path('schema/', get_schema_view(title='API Schema', public=True, permission_classes=[permissions.AllowAny])),
]
