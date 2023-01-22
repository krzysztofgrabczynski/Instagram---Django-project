from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('home')

    form = UserRegistrationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

