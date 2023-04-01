from django.urls import path
from main.views import *
from django.contrib.auth import views as auth_views
from .decorators import if_logged


urlpatterns = [
    path('', home, name='home'),

    path('sign_up/', sign_up, name='sign_up'),
    path('login/', if_logged(auth_views.LoginView.as_view()), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit_password/', auth_views.PasswordChangeView.as_view(template_name='settings/edit_password.html'), name='edit_password'),
    path('', home, name='password_change_done'),

    path('edit_account/<int:id>', edit_account, name='edit_account'),
    path('edit_profile/<int:id>', edit_profile, name='edit_profile'),

    path('profile/<int:id>', user_profile, name='user_profile'),

    path('add_post/', add_post, name='add_post'),
    path('edit_post/<int:id>', edit_post, name='edit_post'),
    path('delete_post/<int:id>', delete_post, name='delete_post'),

    path('add_comment/<int:post_id>', add_comment, name='add_comment'),
    path('delete_comment/<int:id>', delete_comment, name='delete_comment'),

    path('thumb_up/<int:id>', thumb_up, name='thumb_up'),

    path('search/', search, name='search'),

    path('follow/<int:id>', follow, name='follow'),
    path('unfollow/<int:id>', unfollow, name='unfollow'),

]