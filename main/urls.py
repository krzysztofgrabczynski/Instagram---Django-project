from django.urls import path
from main.views import test_view, home, sign_up, login



urlpatterns = [
    path('', home, name='home'),
    path('test/', test_view),
    path('sign_up/', sign_up, name='sign_up'),
    path('login/', login, name='login'),
]