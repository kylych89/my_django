from .models import News
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'info': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }
