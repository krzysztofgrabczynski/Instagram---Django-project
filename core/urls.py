from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("instagram/", include("src.main_old.urls")),
    path("", include("src.user.urls")),
    path("", include("src.post.urls")),
    path("", include("src.comment.urls")),
    path("", include("src.home.urls")),
    path("", include("src.social_actions.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
