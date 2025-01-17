from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Allow null/blank

    def __str__(self):
        return self.user.username

class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')
    likes = models.ManyToManyField(User, related_name='liked_photos', blank=True)

    def __str__(self):
        return self.title
