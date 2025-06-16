from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

# Swagger imports
from .views import schema_view

urlpatterns = [
    path('', lambda request: JsonResponse({
        "status": "success",
        "message": "CP Platform API is live"
    })),

    # Admin and API routes
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('problem_list/', include("problem_list.urls")),
    path('dashboard/', include('dashboard.urls')),

    # Swagger Documentation
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
