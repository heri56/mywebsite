from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'judul': 'Kelas Terbuka',
        'subjudul': 'Selamat Datang',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/contact', 'Contact'],
        ],
        'banner':'img/Cloud_banner.jpg'
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return HttpResponse("Contact")
