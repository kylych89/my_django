from django.shortcuts import render


def index(request):
    context = {
        'title': 'Main page'
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')
