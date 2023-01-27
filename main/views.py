from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User

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

    user_registration_form = UserRegistrationForm()
    return render(request, 'registration/sign_up.html', {'form': user_registration_form})


@login_required
def edit_account(request, id):
    profile = UserProfile.objects.get(user=request.user)
    user = profile.user
    
    user_form = UserRegistrationForm(instance=user)
    
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return redirect(home)

    return render(request, 'account_settings.html', {'user': user_form})

@login_required
def edit_profile(request, id):
    profile = get_object_or_404(UserProfile, pk=id)
    profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if profile_form.is_valid():
        profile_form.save()
        
        return redirect(home)
    print(profile_form.errors)
    return render(request, 'profile_settings.html', {'profile': profile_form})