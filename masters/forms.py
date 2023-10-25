from django import forms
from schedule.models import Today_Task

class TodayForm(forms.ModelForm):
    model = Today_Task
    fields = ('name', 'start_time', 'end_time', 'task')
    
