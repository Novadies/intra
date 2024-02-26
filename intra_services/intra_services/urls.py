from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include

from intra_services.views import pagenotfound
from .views import redirect_page, decorator_redirect_page

urlpatterns = [
    # path('', decorator_redirect_page('search-url')(redirect_page)),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace="users")),
    path('loader/', include('loader.urls', namespace="loader")),
    #path('something/', include('example_something_app.urls', namespace="some_app")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
handler404 = pagenotfound

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Список приложений"

from icecream import install
install()
ic.configureOutput(includeContext=True)  # указание строки и места выполнения

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


