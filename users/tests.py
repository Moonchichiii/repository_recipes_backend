from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.test import TestCase
# Create your tests here.

class UserAccountTests(APITestCase):

    def setUp(self):
        # Create a user that can be used for login tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_registration(self):
        """
        Test to verify user registration.
        """
        data = {
            "username": "newtestuser",
            "email": "newtestuser@example.com",
            "password": "newtestpassword",
            "confirm_password": "newtestpassword"
        }
        response = self.client.post(reverse('users:user-registration'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        """
        Test to verify user login.
        """
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = self.client.post(reverse('users:user-login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_logout(self):
        """
        Test to verify user logout.
        """
        response = self.client.post(reverse('users:user-logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Token.objects.filter(user=self.user).exists())

    def test_user_profile_update(self):
        """
        Test to verify updating user profile image and bio.
        """
        # Assuming 'profiles' is the namespace for profile related URLs
        data = {
            "bio": "New bio",
            "profile_image": None  # Add an actual image here if needed for testing
        }
        response = self.client.patch(reverse('profiles:profile-detail', kwargs={'pk': self.user.profile.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Run the tests
if __name__ == '__main__':
   
