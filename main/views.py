from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm


def home(request):
    return HttpResponse('home_view')

def test_view(request):
    return HttpResponse('test_view')

def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('home')

    form = UserRegistrationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

