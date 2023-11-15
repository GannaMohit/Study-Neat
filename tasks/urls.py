from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDetailView

urlpatterns = [
    path("", TaskListView.as_view(), name='tasks'),
    path("<int:pk>", TaskDetailView.as_view(), name="task"),
    path("new", TaskCreateView.as_view(), name='task_new'),
    path("<int:pk>/edit", TaskUpdateView.as_view(), name="task_edit")
]