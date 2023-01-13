from django import forms
from .models import Student
from django.forms import ModelForm, TextInput


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'age': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            'faculty': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Факультет'
            })
        }
    # faculty = forms.ModelMultipleChoiceField(
    #         queryset=Faculty.objects.all(),
    #         widget=forms.CheckboxSelectMultiple
    #     )

