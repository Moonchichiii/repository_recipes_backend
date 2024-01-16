from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),      
    
    path('comments/', include('comments.urls')),      
    path('likes/', include('likes.urls')),      
    path('followers/', include('followers.urls')),
]

