from django.urls import path
from main.views import home, sign_up, edit_account, edit_profile
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', home, name='home'),
    path('sign_up/', sign_up, name='sign_up'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit_account/<int:id>', edit_account, name='edit_account'),
    path('edit_profile/<int:id>', edit_profile, name='edit_profile')

]