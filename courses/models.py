from django.db import models
from django.urls import reverse
import datetime

def get_current_semester():
    today = datetime.date.today()
    try:
        return Semester.objects.get(start_date__gte = today, end_date__lte = today)
    except:
        return None

class Semester(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name}"

class Course(models.Model):
    subject = models.CharField(max_length=255)
    number = models.CharField(max_length=64)
    nickname = models.CharField(max_length=32)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses', default=get_current_semester)

    def __str__(self):
        return f"{self.nickname}"
    
    def get_absolute_url(self):
        return reverse('courses')
