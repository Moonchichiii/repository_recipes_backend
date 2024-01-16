from rest_framework.authtoken.views import ObtainAuthToken
from django.urls import path
from .views import UserRegistrationView, UserLogoutView



APP_NAME = 'users'
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', ObtainAuthToken.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]
