from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')  

    def create(self, validated_data):
        
        validated_data.pop('confirm_password', None)

        user = User.objects.create_user(**validated_data)
        return user