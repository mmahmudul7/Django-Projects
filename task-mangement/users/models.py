from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile', blank=True, primary_key=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} profile'
