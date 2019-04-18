from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('home.urls', namespace='main_site')),
    path('accounts/',include('accounts.urls')),
    path('master_data/',include('master_data.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
