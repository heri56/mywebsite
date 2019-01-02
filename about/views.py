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
    return render(request, 'about/index.html', context)
