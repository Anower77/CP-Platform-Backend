from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Swagger imports
from .views import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    # # path('', include("home_feed.urls")),
    path('problem_list/', include("problem_list.urls")),
    path('dashboard/', include('dashboard.urls')),
    # path('contest/', include("contest.urls")),
    # path('topics/', include('topics.urls')),

    # Swagger Documentation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
