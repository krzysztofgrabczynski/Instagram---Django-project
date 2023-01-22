from django.urls import path
from main.views import test_view, home, login



urlpatterns = [
    path('', home, name='home'),
    path('test/', test_view),
    path('login/', login, name='login'),
]