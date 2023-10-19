from rest_framework import serializers
from api.models import ProblemsHealth, Client

class ProblemHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemsHealth
        fields = ('name_problem', 'rating')

class ClientSerializer(serializers.ModelSerializer):
    problem_health = ProblemHealthSerializer(many=True)  

    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        problems_data = validated_data.pop('problem_health')
        client = Client.objects.create(**validated_data)

        for problem_data in problems_data:
            problem = ProblemsHealth.objects.create(**problem_data)
            client.problem_health.add(problem)

        return client

class ClientSerializerOrder(serializers.ModelSerializer):
    problem_health = ProblemHealthSerializer(many=True)

    class Meta:
        model = Client
        fields = '__all__'



