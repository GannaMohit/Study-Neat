from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'type', 'course', 'due_date', 'difficulty', 'estimated_time', 'priority', 'file')
        widgets = {
            'due_date': forms.DateInput(attrs={'type':'date'})
        }