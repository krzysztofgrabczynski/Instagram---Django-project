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
            "posts": PostModel.objects.filter(user=self.request.user).order_by("-date")
        }
        context = super().get_context_data(**kwargs)
        context.update(extra_context)
        return context


class EditUserProfileView(ObjectOwnerRequiredMixin, generic.edit.UpdateView):
    model = User
    form_class = EditUserProfileForm
    template_name = "settings/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object_owner(self):
        return self.get_object()
