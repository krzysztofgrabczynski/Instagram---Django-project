from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse('home_view')

def test_view(request):
    return HttpResponse('test_view')
