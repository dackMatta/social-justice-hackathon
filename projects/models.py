from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class LaunchedGovProjects(models.Model):
    STATUS_CHOICES = [
        ('IN_PROGRESS', 'In Progress'),
        ('STALLED', 'Stalled'),
        ('COMPLETED', 'Completed'),
    ]

    project_title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    location = models.CharField(max_length=200)
    launched_by = models.CharField(max_length=200)
    contractor = models.CharField(max_length=200)
    amount_allocated = models.DecimalField(max_digits=15, decimal_places=2)
    overview = models.TextField()
    reporter_name = models.CharField(max_length=200, blank=True, null=True)
    reporter_phone_number = models.CharField(max_length=20, blank=True, null=True)
    project_start_date = models.DateTimeField(auto_now_add=False,null=True)
    project_end_date = models.DateTimeField(auto_now=False,null=True)
    tracked_by = models.ManyToManyField(User, related_name='tracked_projects', blank=True)

    def __str__(self):
        return self.project_title


class ProjectContract(models.Model):
    project = models.ForeignKey(LaunchedGovProjects, on_delete=models.CASCADE, related_name='contracts')
    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='project_contracts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    version = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['project', 'version']

    def __str__(self):
        return f"{self.project.title} - Contract v{self.version}"


