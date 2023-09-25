from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=16)
    number = models.CharField(max_length=64)
    semester = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.number}"