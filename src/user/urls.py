from django.urls import path
from django.contrib.auth import views as auth_views

from src.user import views as user_views


urlpatterns = [
    path("sign_up/", user_views.RegisterUserFormView.as_view(), name="sign_up"),
    path("login/", user_views.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("home/", user_views.home, name="home"),
    # path(
    #     "edit_password/",
    #     auth_views.PasswordChangeView.as_view(
    #         template_name="settings/edit_password.html"
    #     ),
    #     name="edit_password",
    # ),
    # path("", home, name="password_change_done"),
    # path("edit_account/<int:id>", edit_account, name="edit_account"),
    # path("edit_profile/<int:id>", edit_profile, name="edit_profile"),
    # path("profile/<int:id>", user_profile, name="user_profile"),
]
