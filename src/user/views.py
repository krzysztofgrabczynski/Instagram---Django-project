from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect

from src.user.forms import UserRegistrationForm, EditUserProfileForm
from src.user.models import UserProfileModel
from src.user.mixins import RedirectIfLoggedUserMixin, ObjectOwnerRequiredMixin
from src.post.models import PostModel
from src.social_actions.models import FollowModel


class RegisterUserFormView(RedirectIfLoggedUserMixin, generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())


class LoginView(auth_views.LoginView):
    redirect_authenticated_user = True


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = "settings/edit_password.html"
    success_url = reverse_lazy("home")


class UserProfileView(generic.detail.DetailView):
    model = UserProfileModel
    template_name = "user_profile.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        extra_context = {
            "posts": PostModel.objects.filter(user=self.object.user).order_by("-date"),
            "is_followed": self._is_followed(),
            "followers_list": self._followers_list(),
        }
        context = super().get_context_data(**kwargs)
        context.update(extra_context)
        return context

    def _is_followed(self):
        """
        Check if the request.user is following specifi user_profile from request.
        """

        user = self.request.user
        current_profile = self.get_object()
        return (
            True
            if user.follow_source.filter(user_followed=current_profile.user).exists()
            else False
        )

    def _followers_list(self):
        return FollowModel.objects.filter(user_followed=self.object.user)


class EditUserProfileView(ObjectOwnerRequiredMixin, generic.edit.UpdateView):
    model = User
    form_class = EditUserProfileForm
    template_name = "settings/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object_owner(self):
        return self.get_object()
