from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'type', 'course', 'difficulty', 'estimated_time', 'priority', 'file')