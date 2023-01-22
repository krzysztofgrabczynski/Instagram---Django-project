from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegistrationForm


def home(request):
    return HttpResponse('home_view')

def test_view(request):
    return HttpResponse('test_view')

def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        return redirect('home')
    else:
        form = UserRegistrationForm()
        return render(request, 'registration/sign_up.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html')