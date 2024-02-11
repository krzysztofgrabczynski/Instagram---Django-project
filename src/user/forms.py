from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User

from src.user.models import UserProfileModel, GenederChoiceEnum


class UserProfileSaveFormMixin:
    def save(self):
        user = super().save()
        user_profile = {
            "gender": self.cleaned_data["gender"],
            "description": self.cleaned_data["description"],
            "profile_img": self.cleaned_data["profile_img"],
        }

        UserProfileModel.objects.update_or_create(
            user=user,
            defaults=user_profile,
        )

        return user


class UserRegistrationForm(UserProfileSaveFormMixin, auth_forms.UserCreationForm):
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

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with that email already exists")
        return email


class EditUserProfileForm(UserProfileSaveFormMixin, forms.ModelForm):
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
        ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.instance = kwargs.get("instance")
        if self.instance:
            user_profile = self.instance.userprofilemodel
            self.fields["gender"].initial = user_profile.gender
            self.fields["description"].initial = user_profile.description
            self.fields["profile_img"].initial = user_profile.profile_img

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists() and self.instance.email != email:
            raise forms.ValidationError("User with that email already exists")
        return email
