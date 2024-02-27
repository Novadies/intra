from django.urls import path

from example_something_app.views import PsevdoFileLoader

app_name = "some_app"

urlpatterns = [path('files/', PsevdoFileLoader.as_view(), name='files'),
               ]
