from django.urls import path
from main.views import test_view, home


urlpatterns = [
    path('', home),
    path('test/', test_view),
]