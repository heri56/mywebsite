from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'blogkita': '"Blog Saya"',
        'kontributor': 'Heri Prastio',
        'nav': [
            ['/', 'Home'],
            ['/blog/cerita', 'Cerita'],
            ['/blog/news', 'News'],
        ]
    }
    return render(request, 'blog/index.html', context)


def recent(request):
    return HttpResponse('Recent Post')


def news(request):
    context = {
        'blogkita': 'News',
        'kontributor': 'John',
    }
    return render(request, 'blog/index.html', context)


def cerita(request):
    context = {
        'blogkita': 'Cerita',
        'kontributor': 'Kenedy',
    }
    return render(request, 'blog/index.html', context)
