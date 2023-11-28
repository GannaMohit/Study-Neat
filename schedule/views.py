from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Week_Task
from .forms import WeekTaskForm

# Create your views here.
# class CourseListView(ListView):
#     template_name = "courses/courses.html"
#     model = Course

# class CourseDetailView(DetailView):
#     template_name = "courses/course.html"
#     model = Course

class WeekTaskCreateView(CreateView):
    template_name = "schedule/week_task_form.html"
    model = Week_Task
    form_class = WeekTaskForm

# class CourseUpdateView(UpdateView):
#     template_name = "courses/course_form.html"
#     model = Course
#     form_class = CourseForm