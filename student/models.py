from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    age = models.PositiveIntegerField()
    faculty = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/student/{self.id}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
