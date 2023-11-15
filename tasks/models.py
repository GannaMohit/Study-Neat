from django.db import models
from courses.models import Course

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=64, choices=[
       ( "Assignment", "Assignment"),
       ("Reading", "Reading"),
       ("Quiz", "Quiz"),
       ("Exam", "Exam")
    ])
    file = models.FileField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tasks')

    #Attributes
    difficulty = models.IntegerField()
    estimated_time = models.IntegerField() #In Minutes
    priority = models.IntegerField()

    completed = models.BooleanField()

    def __str__(self):
        return f"{self.name}"