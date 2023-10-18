from django.db import models
from courses.models import Task

# Create your models here.
class Week(models.Model):
    number = models.IntegerField()

class Week_Task:
    week = models.ForeignKey(Week, on_delete=models.CASCADE, related_name='tasks')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='week_task')