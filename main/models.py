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
    posts_amount = models.IntegerField(default=0)
    followers_amount = models.IntegerField(default=0)
    following_amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Profile(id:{self.id}): {self.user.username}(id:{self.user.id})'

    def __repr__(self) -> str:
        return self.__str__()

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    user_followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed', default=None)
    followd_user_id = models.PositiveIntegerField(blank=False, default=None)

    def __str__(self) -> str:
        return f'Follow(id:{self.id}): {self.user.username}(id:{self.user.id}) -----> {self.user_followed.username}(id:{self.user_followed.id})'

    def __repr__(self) -> str:
        return self.__str__()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post_img = models.ImageField(upload_to='posts_imgs', blank=False)
    description = models.TextField(default='')
    date = models.DateTimeField(blank=False, auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f'Post of the: {self.user.username}(id:{self.id})'
    
    def __repr__(self) -> str:
        return self.__str__()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(default='')
    date = models.DateTimeField(blank=False, auto_now=True)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Comment(id:{self.id}) of the: {self.user.username}(id:{self.user.id}) under post(id:{self.post.id}) of the: {self.post.user.username}(id:{self.post.user.id})'
    
    def __repr__(self) -> str:
        return self.__str__()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f'Like(id:{self.id}) of the: {self.user.username}(id:{self.user.id}) under post(id:{self.post.id}) of the: {self.post.user.username}'
    
    def __repr__(self) -> str:
        return self.__str__()
        