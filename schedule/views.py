from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Week_Task, Week
from .forms import WeekTaskForm

# Create your views here.
class WeekListView(LoginRequiredMixin, ListView):
    template_name = "schedule/week_tasks.html"
    model = Week_Task

# class CourseDetailView(DetailView):
#     template_name = "courses/course.html"
#     model = Course

class WeekTaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "schedule/week_task_form.html"
    model = Week_Task
    form_class = WeekTaskForm

class WeekTaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "schedule/week_task_form.html"
    model = Week_Task
    form_class = WeekTaskForm