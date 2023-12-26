from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

class ProjectViewSet(ModelViewSet):

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateProjectSerializer
        return serializers.ProjectSerializer
    
    def get_queryset(self):
        return models.Project.objects.filter(user_id = self.request.user.id)
    
    

class TaskViewSet(ModelViewSet):

    def get_queryset(self):
        return models.Task.objects.filter(project_id=self.kwargs['projects_pk'])
    
    def get_serializer_context(self):
        return {"project_id": self.kwargs['projects_pk']}
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return serializers.CreateTaskSerializer
        return serializers.TaskSerializer
