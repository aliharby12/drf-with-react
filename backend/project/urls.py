from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
    path("invoice/", include("invoice.urls")),
]

if settings.DEBUG:  # pragma: no cover

    schema_view = get_schema_view(
        openapi.Info(
            title="Invoice API",
            default_version="1.0",
            description="Invoice API",
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )

    urlpatterns = (
        [
            # Swagger
            path(
                "swagger",
                schema_view.with_ui("swagger", cache_timeout=0),
                name="schema-swagger-ui",
            ),

            # Postman API
            path('postman.json/', schema_view.without_ui(cache_timeout=0),
                 name='schema-postman'),
        ]
        + urlpatterns
        + static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT,
        )
    )
