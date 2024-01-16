from django.db import models
from utils.image_service import upload_image  
from cloudinary.models import CloudinaryField  
from django.contrib.auth import get_user_model

User = get_user_model()  

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = CloudinaryField('image', default='default_pfp_ivf3fa')  

    def __str__(self):
        return f'{self.user.username} Profile'

    # Add a method to save the image using the upload_image function
    def save_profile_image(self, image):
        if image:
            image_url = upload_image(image)
            self.profile_image = image_url
            self.save()
            
    class Meta:
        app_label = 'profiles'
