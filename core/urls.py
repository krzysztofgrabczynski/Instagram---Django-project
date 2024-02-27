from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("src.user.urls")),
    path("", include("src.post.urls")),
    path("", include("src.comment.urls")),
    path("", include("src.home.urls")),
    path("", include("src.social_actions.urls")),
]
