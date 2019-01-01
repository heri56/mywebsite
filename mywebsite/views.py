from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'judul': 'kelas terbuka',
        'kontributor': 'faqihza',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/contact', 'Contact'],
        ]
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return HttpResponse("Contact")
