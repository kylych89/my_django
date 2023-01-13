from django.urls import path
from .views import (
    faculty_view,
    create_faculty_view,
    FacultyDetailView,
    FacultyUpdateView,
    FacultyDeleteView)

app_name = 'faculty'

urlpatterns = [
    # faculty
    path('', faculty_view, name='faculty_view'),
    path('create', create_faculty_view, name='create_faculty_view'),
    path('<int:pk>', FacultyDetailView.as_view(), name='faculty-detail'),
    path('<int:pk>/update', FacultyUpdateView.as_view(), name='faculty-update'),
    path('<int:pk>/delete', FacultyDeleteView.as_view(), name='faculty-delete'),
]
