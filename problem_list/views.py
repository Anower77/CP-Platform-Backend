from rest_framework import viewsets, permissions
from .models import Problem, ProblemStatus
from .serializers import ProblemSerializer, ProblemStatusSerializer

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProblemStatusViewSet(viewsets.ModelViewSet):
    queryset = ProblemStatus.objects.all()  # Needed by DRF router
    serializer_class = ProblemStatusSerializer

    def get_queryset(self):
        return ProblemStatus.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
