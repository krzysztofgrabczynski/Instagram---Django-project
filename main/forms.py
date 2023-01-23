from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    GENDER = [
        (0, 'male'),
        (1, 'female')
    ]

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'password1', 'password2']