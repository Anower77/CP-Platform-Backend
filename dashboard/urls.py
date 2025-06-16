from rest_framework import routers
from django.urls import path, include
from .views import ProblemStatusViewSet, BookmarkViewSet

router = routers.DefaultRouter()
router.register(r'problem-status', ProblemStatusViewSet, basename='problemstatus')
router.register(r'bookmarks', BookmarkViewSet, basename='bookmark')

urlpatterns = [
    path('api/', include(router.urls)),
]
    