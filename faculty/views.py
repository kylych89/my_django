from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from faculty.forms import FacultyForm
from student.models import Faculty


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
