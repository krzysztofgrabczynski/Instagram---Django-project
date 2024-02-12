from django.urls import path
from django.contrib.auth import views as auth_views

from src.user import views as user_views


urlpatterns = [
    path("sign_up/", user_views.RegisterUserFormView.as_view(), name="sign_up"),
    path("login/", user_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("home/", user_views.home, name="home"),
    path(
        "edit_password/",
        user_views.PasswordChangeView.as_view(),
        name="edit_password",
    ),
    path(
        "edit_profile/<int:pk>/",
        user_views.EditUserProfileView.as_view(),
        name="edit_profile",
    ),
    path(
        "profile/<int:pk>/", user_views.UserProfileView.as_view(), name="user_profile"
    ),
]
