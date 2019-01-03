from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'dataabout': 'Judul About',
        'datajudul': 'Selamat datang di About',
        'banner': 'about/img/AboutBanner.png',
        'app_css': 'about/css/style.css',
    }
    return render(request, 'about/index.html', context)
