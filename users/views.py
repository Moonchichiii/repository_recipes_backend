from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny  # Import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, serializers
from .serializers import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    authentication_classes = []  # No authentication required for registration
    permission_classes = [AllowAny]  # Allow any user to register

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        confirm_password = serializer.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return token.key

class UserLogoutView(APIView):
    """
    API view for user logout.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        Delete the user's token to perform logout.
        """
        request.auth.delete()
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
