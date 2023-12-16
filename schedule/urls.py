from django.urls import path
from .views import WeekTaskCreateView, WeekTaskUpdateView

urlpatterns = [
    path("new", WeekTaskCreateView.as_view(), name='week_task_new'),
    path("<int:pk>", WeekTaskUpdateView.as_view(), name='week_task_edit')
]