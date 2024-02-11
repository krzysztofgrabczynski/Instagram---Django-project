from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

from src.user.forms import UserRegistrationForm, EditUserProfileForm
from src.user.models import UserProfileModel


class RegisterUserFormView(generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy("home")


class LoginView(auth_views.LoginView):
    redirect_authenticated_user = True


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = "settings/edit_password.html"
    success_url = reverse_lazy("home")


class EditUserProfileView(generic.edit.UpdateView):
    model = User
    form_class = EditUserProfileForm
    template_name = "settings/edit_profile.html"
    success_url = reverse_lazy("home")


def home(request):
    return HttpResponse("home")
