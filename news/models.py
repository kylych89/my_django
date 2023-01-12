from django.db import models


class News(models.Model):
    title = models.CharField('Название', max_length=50)
    info = models.TextField('Статья')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


