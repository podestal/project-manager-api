from rest_framework_nested import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()

router.register('projects', views.ProjectViewSet)

projects_router = routers.NestedDefaultRouter(router, 'projects', lookup='projects')
projects_router.register('tasks', views.TaskViewSet, basename='tasks')

urlpatterns = router.urls + projects_router.urls