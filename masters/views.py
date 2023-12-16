from django.shortcuts import render
from django.views.generic import ListView
from masters.forms import TodayForm
from schedule.models import Week_Task, Week

# Create your views here.
class DashboardView(ListView):
    template_name = 'masters/dashboard.html'
    model = Week_Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodayForm
        return context