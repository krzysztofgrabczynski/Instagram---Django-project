from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User

from src.user.models import UserProfileModel, GenederChoiceEnum


class UserRegistrationForm(auth_forms.UserCreationForm):
    gender = forms.ChoiceField(choices=GenederChoiceEnum.choices)
    description = forms.CharField(widget=forms.Textarea)
    profile_img = forms.ImageField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(seld):
        email = seld.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with that email already exists")
        return email

    def save(self):
        user = super().save()
        user_profile = {
            "gender": self.cleaned_data["gender"],
            "description": self.cleaned_data["description"],
            "profile_img": self.cleaned_data["profile_img"],
        }

        UserProfileModel.objects.create(
            user=user,
            **user_profile,
        )
        return user
