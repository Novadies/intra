from django.urls import path
from django.views.decorators.cache import cache_page

from loader.views import FileLoader

app_name = "loader"

urlpatterns = [
    path('files/', FileLoader.as_view(), name='files'),
]
