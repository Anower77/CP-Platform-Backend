from rest_framework import serializers
from .models import ProblemStatus, Bookmark

class ProblemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemStatus
        fields = ['id', 'user', 'problem', 'status', 'bookmarked']
        ref_name = "Dashboard_ProblemStatus"

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'problem', 'created_at']
