from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Student, Faculty
from .forms import StudentForm, FacultyForm
from django.views.generic import DetailView, UpdateView, DeleteView


def student_view(request):
    student = Student.objects.all()
    return render(request, 'main/student/student.html', {'student': student})


class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student/student_detail_view.html'
    context_object_name = 'student'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'main/student/create_student_view.html'
    form_class = StudentForm


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/student/'
    template_name = 'main/student/student-delete.html'


def create_student_view(request):
    error = ''

    if request.method == 'POST':
        form = StudentForm(request.POST)
        faculty = Faculty.objects.all()
        if form.is_valid():
            obj = faculty.form.cleaned_data['name']
            form.save()
            return redirect('main:home')
        else:
            error = 'Wrong'

    form = StudentForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/student/create_student_view.html', context)


def faculty_view(request):
    faculty = Faculty.objects.all()
    context = {
        'faculty': faculty,
    }
    return render(request, 'main/faculty/faculty.html', context)


def create_faculty_view(request):
    error = ''

    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
        else:
            error = 'Wrong'

    form = FacultyForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/faculty/create_faculty_view.html', context)


class FacultyDetailView(DetailView):
    model = Faculty
    template_name = 'main/faculty/faculty_detail_view.html'
    context_object_name = 'faculty'


class FacultyUpdateView(UpdateView):
    model = Faculty
    template_name = 'main/faculty/create_faculty_view.html'
    form_class = FacultyForm


class FacultyDeleteView(DeleteView):
    model = Faculty
    success_url = '/student/'
    template_name = 'main/faculty/faculty-delete.html'
