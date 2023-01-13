from django.shortcuts import render, redirect

from faculty.forms import FacultyForm
from .models import Student
from .forms import StudentForm
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
        form_faculty = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            form_faculty.save()
            return redirect('main:home')
        else:
            error = 'Wrong'

    form = StudentForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/student/create_student_view.html', context)

