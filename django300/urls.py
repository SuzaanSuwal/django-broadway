from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# from myapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', include('crud.urls')),
    path('', include('myapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


