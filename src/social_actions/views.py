from typing import Any
from typing import Union

from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

from src.social_actions.models import FollowModel, LikeModel
from src.user.models import UserProfileModel


class FollowActionView(generic.RedirectView):
    url = None

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        user_profile = self.get_user_profile_from_request(kwargs.get("pk"))
        if request.user == user_profile.user:
            self.url = reverse_lazy("home")

        follow = self.check_if_user_is_following(request.user, user_profile)
        if follow:
            self.unfollow(request.user, user_profile, follow)
        else:
            self.follow(request.user, user_profile)

        self.url = reverse_lazy("user_profile", kwargs={"pk": user_profile.pk})

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
