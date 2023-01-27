from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserProfile(models.Model):
    GENDER = [
        (1, 'male'),
        (2, 'female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.PositiveSmallIntegerField(choices=GENDER, default=1)
    description = models.TextField(default='')
    profile_img = models.ImageField(upload_to='profile_imgs', blank=True, null=True)

    def __str__(self) -> str:
        return f'Profile: {self.user.username}'

    def __repr__(self) -> str:
        return self.__str__()