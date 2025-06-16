from rest_framework import viewsets
from .models import ProblemStatus, Bookmark
from .serializers import ProblemStatusSerializer, BookmarkSerializer
from rest_framework.permissions import IsAuthenticated

class ProblemStatusViewSet(viewsets.ModelViewSet):
    serializer_class = ProblemStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only records for logged-in user, ordered by last_updated
        return ProblemStatus.objects.filter(user=self.request.user).order_by('-last_updated')

    def perform_create(self, serializer):
        # Set the user to the logged-in user automatically
        serializer.save(user=self.request.user)

class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only records for logged-in user, ordered by creation date
        return Bookmark.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
