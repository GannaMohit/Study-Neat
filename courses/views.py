from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from .forms import CourseForm
from .models import Course

# Create your views here.
class CourseListView(ListView):
    template_name = "courses/courses.html"
    model = Course


class CourseCreateView(CreateView):
    template_name = "courses/course_form.html"
    model = Course
    form_class = CourseForm

class CourseUpdateView(UpdateView):
    template_name = "courses/course_form.html"
    model = Course
    form_class = CourseForm