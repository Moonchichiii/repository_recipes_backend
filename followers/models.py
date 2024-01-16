from django.db import models
from profiles.models import Profile
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')  
        constraints = [
            models.CheckConstraint(check=~models.Q(follower=models.F('following')), name='cannot_follow_self'),
        ]

    def __str__(self):
        return f"{self.follower.user.username} follows {self.following.user.username}"
