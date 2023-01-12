from django.urls import path
from .views import index, about

app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
]
