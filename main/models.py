from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(default='')
    profile_img = models.ImageField(upload_to='profile_imgs', blank=True, null=True)
