from django import forms
from .models import Week_Task

class WeekTaskForm(forms.ModelForm):
    class Meta:
        model = Week_Task
        fields = ('week_number', 'name', 'task', 'date', 'start_time', 'end_time')
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'start_time': forms.TimeInput(attrs={'type':'time'}),
            'end_time': forms.TimeInput(attrs={'type':'time'})
        }