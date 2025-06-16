from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProblemViewSet, ProblemStatusViewSet

router = DefaultRouter()
router.register(r'problems', ProblemViewSet)
router.register(r'status', ProblemStatusViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
