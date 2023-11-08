from django.urls import path
from .views import CourseListView, CourseCreateView, CourseUpdateView

urlpatterns = [
    path("", CourseListView.as_view(), name='courses'),
    path("new", CourseCreateView.as_view(), name='course_new'),
    path("<int:pk>/edit", CourseUpdateView.as_view(), name="course_edit")
]