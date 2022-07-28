from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    context = {
        'title': 'Продукты',
    }
    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', context=context)
