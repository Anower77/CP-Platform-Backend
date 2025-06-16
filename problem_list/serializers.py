from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Problem, ProblemStatus

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class ProblemStatusSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    problem = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProblemStatus
        fields = '__all__'
        ref_name = "ProblemList_ProblemStatus"
