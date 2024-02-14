from django.urls import path
from src.comment import views as user_views


urlpatterns = [
    path(
        "add_comment/<int:pk>/",
        user_views.CreateCommentView.as_view(),
        name="add_comment",
    ),
    path(
        "delete_comment/<int:pk>/",
        user_views.DeleteCommentView.as_view(),
        name="delete_comment",
    ),
]
