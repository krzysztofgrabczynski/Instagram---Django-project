from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserProfile(models.Model):
    GENDER = [
        (0, 'male'),
        (1, 'female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.PositiveSmallIntegerField(choices=GENDER, default=0)
    description = models.TextField(default='', blank=True)
    profile_img = models.ImageField(default='profile_imgs/default_male.jpg', upload_to='profile_imgs', blank=True, null=True)
    photos = 0
    followers = 0
    following = 0

    def __str__(self) -> str:
        return f'Profile: {self.user.username}'

    def __repr__(self) -> str:
        return self.__str__()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post_img = models.ImageField(upload_to='posts_imgs', blank=False)
    description = models.TextField(default='')
    date = models.DateTimeField(blank=False, auto_now=True)
    likes = 0
    
    def __str__(self) -> str:
        return f'Post of the: {self.user.username}'
    
    def __repr__(self) -> str:
        return self.__str__()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(default='')
    date = models.DateTimeField(blank=False, auto_now=True)
    likes = 0

    def __str__(self) -> str:
        return f'Comment of the: {self.user.username} under post of the: {self.post.user.username}'
    
    def __repr__(self) -> str:
        return self.__str__()

        