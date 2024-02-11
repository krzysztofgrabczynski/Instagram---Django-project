from django.db import models
from django.contrib.auth import get_user_model
from enum import Enum


User = get_user_model()


class GenederChoiceEnum(models.IntegerChoices):
    MALE = 0
    FEMALE = 1


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    gender = models.PositiveSmallIntegerField(
        choices=GenederChoiceEnum.choices, default=GenederChoiceEnum.MALE
    )
    description = models.TextField(default="")
    profile_img = models.ImageField(
        default="profile_imgs/default_male.jpg",
        upload_to="profile_imgs",
    )
    posts_amount = models.IntegerField(default=0)
    followers_amount = models.IntegerField(default=0)
    following_amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Profile(id:{self.id}): {self.user.username}(id:{self.user.id})"

    def __repr__(self) -> str:
        return self.__str__()
