from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm


@login_required
def home(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.method == 'POST':
        user_registration_form = UserRegistrationForm(request.POST or None)
        user_profile_form = UserProfileForm()
        if user_registration_form.is_valid():
            user_profile = user_profile_form.save(commit=False)
            user = user_registration_form.save()
            user_profile.user = user
            user_profile.save()

            login(request, user)
            return redirect('home')

        else:
            print(user_registration_form.errors)
    user_registration_form = UserRegistrationForm()
    return render(request, 'registration/sign_up.html', {'form': user_registration_form})

