from django.urls import path
from .views import CourseListView, CourseCreateView, CourseUpdateView, CourseDetailView

urlpatterns = [
    path("", CourseListView.as_view(), name='courses'),
    path("<int:pk>", CourseDetailView.as_view(), name="course"),
    path("new", CourseCreateView.as_view(), name='course_new'),
    path("<int:pk>/edit", CourseUpdateView.as_view(), name="course_edit")
]