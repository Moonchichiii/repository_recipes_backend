from django.urls import path
from . import views

urlpatterns = [
    path('follows/', views.FollowViewSet.as_view({'get': 'list', 'post': 'create'}), name='follow-list'),
    path('follows/<int:pk>/', views.FollowViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='follow-detail'),
    path('follows/following/', views.FollowViewSet.as_view({'get': 'following'}), name='following-list'),
    path('follows/followers/', views.FollowViewSet.as_view({'get': 'followers'}), name='followers-list'),
 
]