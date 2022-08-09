from django.shortcuts import render

from mainapp.models import Products


MENU_LINKS = {
    'index': 'Главная',
    'products': 'Продукты',
    'contact': 'Контакты',
}


def index(request):
    context = {
        'title': 'Главная',
        'menu': MENU_LINKS,
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    context = {
        'title': 'Продукты',
        'menu': MENU_LINKS,
        'main_product': ['img/controll.jpg', 'img/controll1.jpg', 'img/controll2.jpg'],
        'products': Products.objects.all()
    }
    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты',
        'menu': MENU_LINKS,
    }
    return render(request, 'mainapp/contact.html', context=context)
