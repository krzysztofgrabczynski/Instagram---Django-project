from typing import Union

from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from src.social_actions.models import FollowModel, LikeModel
from src.user.models import UserProfileModel
from src.post.models import PostModel
from src.mixins import SetLastVisitedUrl


@method_decorator(SetLastVisitedUrl(), name="dispatch")
class FollowActionView(LoginRequiredMixin, generic.RedirectView):
    url = None

    def get(self, request, *args, **kwargs):
        user_profile = self.get_user_profile_from_request(kwargs.get("pk"))
        if request.user == user_profile.user:
            self.url = reverse_lazy("home")

        follow = self.check_if_user_is_following(request.user, user_profile)
        if follow:
            self.unfollow(request.user, user_profile, follow)
        else:
            self.follow(request.user, user_profile)

        return super().get(request, *args, **kwargs)

    def get_user_profile_from_request(self, pk: int) -> UserProfileModel:
        return UserProfileModel.objects.get(id=pk)

    def check_if_user_is_following(
        self, user: User, user_profile: UserProfileModel
    ) -> Union[None, FollowModel]:
        """
        @param user: logged in user that want to follow the owner of the user_profile (other user)
        @param user_profile: profile of the user that will be followed by the logged in user
        """

        follow_obj = user.follow_source.filter(user_followed=user_profile.user)
        return follow_obj if follow_obj else None

    def follow(self, user: User, user_profile: UserProfileModel) -> None:
        """
        @param user: logged in user that want to follow the owner of the user_profile (other user)
        @param user_profile: profile of the user that will be followed by the logged in user
        """

        new_follow = FollowModel.objects.create(
            user=user, user_followed=user_profile.user
        )
        new_follow.save()

        user.userprofilemodel.following_amount += 1
        user.userprofilemodel.save()
        user_profile.followers_amount += 1
        user_profile.save()

    def unfollow(
        self, user: User, user_profile: UserProfileModel, follow: FollowModel
    ) -> None:
        """
        @param user: logged in user that want to follow the owner of the user_profile (other user)
        @param user_profile: profile of the user that will be followed by the logged in user
        @param follow: FollowModel object that will be removed
        """

        follow.delete()

        user.userprofilemodel.following_amount -= 1
        user.userprofilemodel.save()
        user_profile.followers_amount -= 1
        user_profile.save()


@method_decorator(SetLastVisitedUrl(), name="dispatch")
class LikeActionView(LoginRequiredMixin, generic.RedirectView):
    url = None

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        for like in post.likemodel_set.all():
            if like in request.user.likemodel_set.all():
                self.delete_like(like, post)
                break
        else:
            self.create_like(request.user, post)

        return super().get(request, *args, **kwargs)

    def get_object(self) -> PostModel:
        """
        That function can raise an exception AttributeError if `pk` of the object is not present in `self.kwargs`.
        """

        pk = self.kwargs.get("pk")

        if pk is not None:
            return PostModel.objects.get(pk=pk)

        raise AttributeError("Missing 'pk' in the URLconf.")

    def create_like(self, user: User, post: PostModel) -> None:
        new_like = LikeModel.objects.create(user=user, post=post)
        new_like.save()
        post.likes += 1
        post.save()

    def delete_like(self, like: LikeModel, post: PostModel) -> None:
        like.delete()
        post.likes -= 1
        post.save()
