from django.urls import path
from django.contrib.auth.views import LoginView
from masters.views import DashboardView

urlpatterns = [
    path("", LoginView.as_view(template_name='masters/login.html'), name='login'),
    path("dashboard", DashboardView.as_view(), name='dashboard')
]
