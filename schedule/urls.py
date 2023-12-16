from django.urls import path
from .views import WeekListView, WeekTaskCreateView, WeekTaskUpdateView

urlpatterns = [
    path("weeks", WeekListView.as_view(), name='week_tasks'),
    path("new", WeekTaskCreateView.as_view(), name='week_task_new'),
    path("<int:pk>/edit", WeekTaskUpdateView.as_view(), name='week_task_edit')
]