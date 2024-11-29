from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

menu = ['О сайте', 'Одежда для кукол', 'Обувь для кукол', 'Хвастики', 'Войти']

typ_clothing = [
    {'id': 1, 'title': 'Свитшот для куклы Paola Reina', 'content': 'Характеристики и описание', 'аvailability': True},
    {'id': 2, 'title': 'Блузка для куклы Paola Reina', 'content': 'Характеристики и описание', 'аvailability': True},
    {'id': 3, 'title': 'Наушники для кукол', 'content': 'Характеристики и описание', 'аvailability': True}
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'dolls/index.html', data)


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id:{cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id:{cat_slug}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def clothes(request):
    data = {
        'title': 'Одежда для кукол',
        'typ_clothing': typ_clothing,
    }
    return render(request, 'dolls/clothes.html', data)
