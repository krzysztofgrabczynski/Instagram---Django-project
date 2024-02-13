from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to="posts_imgs")
    description = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Post of the: {self.user.username}(id:{self.id})"

    def __repr__(self) -> str:
        return self.__str__()
