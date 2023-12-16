from django.db import models
from django.urls import reverse
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
    due_date = models.DateField()
    file = models.FileField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tasks')

    #Attributes
    difficulty = models.IntegerField()
    estimated_time = models.IntegerField() #In Minutes
    priority = models.IntegerField()

    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('tasks')