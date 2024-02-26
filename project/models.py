from django.db import models
from django.conf import settings



class Project(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Task(models.Model):

    STATUS_NOT_STARTED = "N"
    STATUS_IN_PROGRESS = "P"
    STATUS_IN_REVISION = "R"
    STATUS_COMPLETED = "C"

    STATUS_CHOICES = [
        (STATUS_NOT_STARTED, "Not Started"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_IN_REVISION, "In Revision"),
        (STATUS_COMPLETED, "Completed")
    ]

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_NOT_STARTED)
    created_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")

