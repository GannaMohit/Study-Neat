from django import forms
from schedule.models import Today_Task

class TodayForm(forms.ModelForm):
    class Meta:
        model = Today_Task
        fields = ('name', 'task', 'completed')
    
