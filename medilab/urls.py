
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include

from medilab import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', include('medilabApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
