from django.urls import path
from src.post import views as user_views


urlpatterns = [
    path("add_post/", user_views.CreatePostView.as_view(), name="add_post"),
    path("edit_post/<int:pk>/", user_views.EditPostView.as_view(), name="edit_post"),
    path(
        "delete_post/<int:pk>/", user_views.DeletePostView.as_view(), name="delete_post"
    ),
]
