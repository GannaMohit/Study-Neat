from django.shortcuts import render
from django.views.generic import TemplateView
from masters.forms import TodayForm

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'masters/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodayForm
        return context