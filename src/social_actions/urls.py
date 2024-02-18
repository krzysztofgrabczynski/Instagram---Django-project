from django.urls import path

from src.social_actions import views as user_views


urlpatterns = [
    path("follow/<int:pk>/", user_views.FollowActionView.as_view(), name="follow"),
    path("unfollow/<int:pk>/", user_views.FollowActionView.as_view(), name="unfollow"),
    path("like/<int:pk>/", user_views.LikeActionView.as_view(), name="like"),
]
