from django.contrib import admin
from django.urls import path, include
from .urls_api import urlpatterns_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urlpatterns_api)),
]
