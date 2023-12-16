from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Week_Task, Week
from .forms import WeekTaskForm

# Create your views here.
class WeekListView(ListView):
    template_name = "schedule/weeks.html"
    model = Week

# class CourseDetailView(DetailView):
#     template_name = "courses/course.html"
#     model = Course

class WeekTaskCreateView(CreateView):
    template_name = "schedule/week_task_form.html"
    model = Week_Task
    form_class = WeekTaskForm

class WeekTaskUpdateView(UpdateView):
    template_name = "schedule/week_task_form.html"
    model = Week_Task
    form_class = WeekTaskForm