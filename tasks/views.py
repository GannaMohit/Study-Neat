from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskListView(ListView):
    template_name = "tasks/tasks.html"
    model = Task

class TaskDetailView(DetailView):
    template_name = "tasks/task.html"
    model = Task

class TaskCreateView(CreateView):
    template_name = "tasks/task_form.html"
    model = Task
    form_class = TaskForm

class TaskUpdateView(UpdateView):
    template_name = "tasks/task_form.html"
    model = Task
    form_class = TaskForm