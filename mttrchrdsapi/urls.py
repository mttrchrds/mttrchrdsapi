from django.contrib import admin
from django.urls import path, include
from .urls_endpoints import urlpatterns_endpoints
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    title='mttrchrds API',
    url='/api/',
    patterns=urlpatterns_endpoints,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urlpatterns_endpoints)),
    path('openapi', schema_view, name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
