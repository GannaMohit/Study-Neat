from django.shortcuts import render
from django.views.generic import TemplateView
from masters.forms import TodayForm
from tasks.models import Task
from schedule.models import Week_Task, Week, get_current_week

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'masters/dashboard.html'
    model = Week_Task
    week = get_current_week()
    queryset = week.tasks.all() if week is not None else []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['week'] = get_current_week()
        context['tasks'] = Task.objects.filter(completed=False).order_by('due_date')
        return context