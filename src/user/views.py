from django.views import generic
from django.contrib.auth.models import User

from src.user.forms import UserRegistrationForm


class RegisterUserFormView(generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration/sign_up.html"
    success_url = ...  # home
