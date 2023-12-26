from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

class ProjectViewSet(ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

class TaskViewSet(ModelViewSet):

    def get_queryset(self):
        return models.Task.objects.filter(project_id=self.kwargs['projects_pk'])
    
    def get_serializer_context(self):
        return {"project_id": self.kwargs['projects_pk']}
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return serializers.CreateTaskSerializer
        return serializers.TaskSerializer
