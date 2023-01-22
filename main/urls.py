from django.urls import path
from main.views import test_view, home, sign_up
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', home, name='home'),
    path('test/', test_view),
    path('sign_up/', sign_up, name='sign_up'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]