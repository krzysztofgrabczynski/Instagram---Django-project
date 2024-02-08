from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

from src.user.forms import UserRegistrationForm


class RegisterUserFormView(generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration/sign_up.html"
    success_url = ...  # home


class CustomLoginView(auth_views.LoginView):
    redirect_authenticated_user = True


def home(request):
    return HttpResponse("home")
