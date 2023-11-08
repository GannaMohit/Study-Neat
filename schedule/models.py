from django.db import models
from courses.models import Task

# Create your models here.

class Today_Task(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='today_task', blank=True, null=True)
    completed = models.BooleanField()

class Week_Task:
    name = models.CharField(max_length=255)
    week_number = models.IntegerField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='week_task', blank=True, null=True)

