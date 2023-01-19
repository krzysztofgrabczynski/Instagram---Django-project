from django.urls import path
from main.views import test_view


urlpatterns = [
    path('test/', test_view),
]