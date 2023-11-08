from django.urls import path
from .views import CourseCreateView

urlpatterns = [
    path("new", CourseCreateView.as_view(), name='course_new')
]