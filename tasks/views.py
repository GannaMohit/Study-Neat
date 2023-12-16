from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskListView(LoginRequiredMixin, ListView):
    template_name = "tasks/tasks.html"
    model = Task

class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = "tasks/task.html"
    model = Task

class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "tasks/task_form.html"
    model = Task
    form_class = TaskForm

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "tasks/task_form.html"
    model = Task
    form_class = TaskForm