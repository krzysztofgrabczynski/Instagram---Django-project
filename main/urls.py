from django.urls import path
from main.views import home, sign_up, edit_account, edit_profile, user_profile, add_post, add_comment
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('sign_up/', sign_up, name='sign_up'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit_password/', auth_views.PasswordChangeView.as_view(template_name='settings/edit_password.html'), name='edit_password'),
    path('', home, name='password_change_done'),
    path('edit_account/<int:id>', edit_account, name='edit_account'),
    path('edit_profile/<int:id>', edit_profile, name='edit_profile'),
    path('profile/<int:id>', user_profile, name='user_profile'),
    path('add_post/', add_post, name='add_post'),
    path('add_comment/<int:post_id>', add_comment, name='add_comment'),

]