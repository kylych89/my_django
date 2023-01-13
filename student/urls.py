from django.urls import path
from .views import (student_view,
                    create_student_view,
                    StudentDetailView,
                    StudentUpdateView,
                    StudentDeleteView,
                    faculty_view,
                    create_faculty_view,
                    FacultyDetailView,
                    FacultyUpdateView,
                    FacultyDeleteView)

app_name = 'student'

urlpatterns = [
    path('', student_view, name='student_view'),
    path('create', create_student_view, name='create_student_view'),
    path('<int:pk>', StudentDetailView.as_view(), name='student-detail'),
    path('<int:pk>/update', StudentUpdateView.as_view(), name='student-update'),
    path('<int:pk>/delete', StudentDeleteView.as_view(), name='student-delete'),

    # faculty
    path('', faculty_view, name='faculty_view'),
    path('create', create_faculty_view, name='create_faculty_view'),
    path('<int:pk>', FacultyDetailView.as_view(), name='faculty-detail'),
    path('<int:pk>/update', FacultyUpdateView.as_view(), name='faculty-update'),
    path('<int:pk>/delete', FacultyDeleteView.as_view(), name='faculty-delete'),
]
