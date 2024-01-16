from utils.serializers import ImageUploadMixin
from .models import Profile

class ProfileSerializer(ImageUploadMixin, serializers.ModelSerializer):
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