from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from django.forms import ModelForm


class UserRegistrationForm(UserCreationForm):
    GENDER = [
        (0, 'male'),
        (1, 'female')
    ]

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    # gender = forms.ChoiceField(choices=GENDER, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'description', 'profile_img']