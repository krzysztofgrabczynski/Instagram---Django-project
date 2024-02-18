from django.urls import path

from src.home import views as user_views


urlpatterns = [
    path("home/", user_views.HomeView.as_view(), name="home"),
    path("search/", user_views.Search.as_view(), name="search"),
]
