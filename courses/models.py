from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=16)
    number = models.CharField(max_length=64)
    semester = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.number}"
    
class Task(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(choices=[
       ( "Assignment", "Assignment"),
       ("Reading", "Reading"),
       ("Quiz", "Quiz"),
       ("Exam", "Exam")
    ])
    file = models.FileField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tasks')

    #Attributes
    difficulty = models.IntegerField(min=1, max=10)
    estimated_time = models.IntegerField() #In Minutes
    priority = models.IntegerField(min=1, max=5)

    def __str__(self):
        return f"{self.name}"