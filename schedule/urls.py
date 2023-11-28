from django.urls import path
from .views import WeekTaskCreateView

urlpatterns = [
    path("new", WeekTaskCreateView.as_view(), name='week_task_new'),
]