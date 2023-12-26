from rest_framework import serializers
from . import models

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'
    
class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ['title']

    def create(self, validated_data):
        project_id = self.context['project_id']
        return models.Task.objects.create(project_id = project_id, **validated_data)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'
