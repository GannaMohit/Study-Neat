from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CourseForm
from .models import Course

# Create your views here.
class CourseListView(LoginRequiredMixin, ListView):
    template_name = "courses/courses.html"
    model = Course

class CourseDetailView(LoginRequiredMixin, DetailView):
    template_name = "courses/course.html"
    model = Course

class CourseCreateView(LoginRequiredMixin, CreateView):
    template_name = "courses/course_form.html"
    model = Course
    form_class = CourseForm

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "courses/course_form.html"
    model = Course
    form_class = CourseForm