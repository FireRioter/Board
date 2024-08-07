from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # URL для allauth
    path('', include("protect.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('sign/', include('sign.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)