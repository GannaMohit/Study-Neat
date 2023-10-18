from django.db import models

class Semester(models.Model):
    name = models.CharField(64)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name}"

class Course(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=16)
    number = models.CharField(max_length=64)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')

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
    difficulty = models.IntegerField()
    estimated_time = models.IntegerField() #In Minutes
    priority = models.IntegerField()

    completed = models.BooleanField()

    def __str__(self):
        return f"{self.name}"