from rest_framework import serializers

from api.models import ProblemsHealth, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['problem_health']

        