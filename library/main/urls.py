from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kurlib.urls')),
    path('about/', include('aboutlibrary.urls')),
    path('reader/', include('reader.urls')),
    path('kraevedenie', include('localhistory.urls')),
    path('events/', include('events.urls')),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
