from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment
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
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender', 'description', 'profile_img']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_img', 'description']
    
class CommentForm(ModelForm):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Add a comment','rows': 1, 'cols': 69}))
    class Meta:
        model = Comment
        fields = ['text']