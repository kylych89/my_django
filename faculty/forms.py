from django.forms import ModelForm, TextInput
from student.models import Faculty


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            })
        }