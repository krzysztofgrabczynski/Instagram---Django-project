from django.db import models
from django.contrib.auth import get_user_model

from src.post.models import PostModel


User = get_user_model()


class FollowModel(models.Model):
    """
    @param user: (follow_source) is a user that what to follow other user
    @param user_followed: (follow_dest) is a user that will be followed by other user
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follow_source"
    )
    user_followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follow_dest"
    )

    def __str__(self) -> str:
        return f"Follow(id:{self.id}): {self.user.username}(id:{self.user.id}) -----> {self.user_followed.username}(id:{self.user_followed.id})"

    def __repr__(self) -> str:
        return self.__str__()


class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Like(id:{self.id}) of the: {self.user.username}(id:{self.user.id}) under post(id:{self.post.id}) of the: {self.post.user.username}"

    def __repr__(self) -> str:
        return self.__str__()
