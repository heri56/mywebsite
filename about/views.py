from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'dataabout': 'Judul About',
        'datajudul': 'Selamat datang di About',
        'banner': 'about/img/AboutBanner.png',
    }
    return render(request, 'about/index.html', context)
