from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_view(request):
    news = News.objects.all()
    return render(request, 'main/news/news.html', {'news': news})


class NewsDetailView(DetailView):
    model = News
    template_name = 'main/news/details_view.html'
    context_object_name = 'news'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'main/news/create_news.html'
    form_class = NewsForm


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'main/news/news_delete.html'


def create_view(request):
    error = ''

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
        else:
            error = 'Wrong'

    form = NewsForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/news/create_news.html', context)
