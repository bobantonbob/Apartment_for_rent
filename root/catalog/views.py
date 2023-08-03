from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html', {
        'title': 'Каталог',
        'page': 'index',
        'app': 'catalog'
    })




