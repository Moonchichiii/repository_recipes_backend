from django.db import models
from utils.image_service import upload_image
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from rest_framework import serializers  

from .models import Profile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):

    profile_image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('profile_image', None)
        profile = super().create(validated_data)
        self.validate_image(image)
        return self.save_image(profile, 'profile_image', image)

    def update(self, instance, validated_data):
        image = validated_data.pop('profile_image', None)
        self.validate_image(image)
        return self.save_image(instance, 'profile_image', image)