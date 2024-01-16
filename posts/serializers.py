from rest_framework import serializers
from utils.serializers import ImageUploadMixin 
class PostSerializer(ImageUploadMixin, serializers.ModelSerializer):
    post_image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('post_image', None)
        post = super().create(validated_data)
        self.validate_image(image)
        return self.save_image(post, 'post_image', image)

    def update(self, instance, validated_data):
        image = validated_data.pop('post_image', None)
        self.validate_image(image)
        return self.save_image(instance, 'post_image', image)