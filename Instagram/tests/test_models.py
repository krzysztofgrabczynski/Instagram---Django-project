from django.test import TestCase
from main.models import UserProfile, Follow, Post, Comment, Like
from django.contrib.auth.models import User


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="David",
            first_name="David",
            last_name="Jones",
            email="david@example.com",
            password="PasswordExample123!",
        )
        User.objects.create_user(
            username="test_username",
            first_name="test_first_name",
            last_name="test_last_name",
            email="test1@example.com",
            password="PasswordExample123!",
        )
        UserProfile.objects.create(
            user=User.objects.get(id=1), description="Test description"
        )
        Follow.objects.create(
            user=User.objects.get(id=1),
            user_followed=User.objects.get(id=2),
            followd_user_id=User.objects.get(id=2).id,
        )
        Post.objects.create(user=User.objects.get(id=1), description="Test description")
        Comment.objects.create(
            post=Post.objects.get(id=1), user=User.objects.get(id=1), text="Test text"
        )
        Like.objects.create(user=User.objects.get(id=1), post=Post.objects.get(id=1))

    def test_UserProfile_model__str__(self):
        test_user_1_profile = UserProfile.objects.get(id=1)
        expected = f"Profile(id:{test_user_1_profile.id}): {test_user_1_profile.user.username}(id:{test_user_1_profile.user.id})"

        self.assertEqual(expected, str(test_user_1_profile))

    def test_Follow_model__str__(self):
        test_follow = Follow.objects.get(id=1)
        expected = f"Follow(id:{test_follow.id}): {test_follow.user.username}(id:{test_follow.user.id}) -----> {test_follow.user_followed.username}(id:{test_follow.user_followed.id})"

        self.assertEqual(expected, str(test_follow))

    def test_Post_model__str__(self):
        test_post = Post.objects.get(id=1)
        expected = f"Post of the: {test_post.user.username}(id:{test_post.id})"

        self.assertEqual(expected, str(test_post))

    def test_Comment_model__str__(self):
        test_comment = Comment.objects.get(id=1)
        expected = f"Comment(id:{test_comment.id}) of the: {test_comment.user.username}(id:{test_comment.user.id}) under post(id:{test_comment.post.id}) of the: {test_comment.post.user.username}(id:{test_comment.post.user.id})"

        self.assertEqual(expected, str(test_comment))

    def test_Like_model__str__(self):
        test_like = Like.objects.get(id=1)
        expected = f"Like(id:{test_like.id}) of the: {test_like.user.username}(id:{test_like.user.id}) under post(id:{test_like.post.id}) of the: {test_like.post.user.username}"

        self.assertEqual(expected, str(test_like))
