from django.db import models
from tasks.models import Task

# Create your models here.

class Week(models.Model):
    number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.number}"

class Today_Task(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='today_task', blank=True, null=True)
    completed = models.BooleanField()

class Week_Task(models.Model):
    name = models.CharField(max_length=255)
    week_number = models.ForeignKey(Week, on_delete=models.CASCADE, related_name='tasks')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='week_task', blank=True, null=True)

