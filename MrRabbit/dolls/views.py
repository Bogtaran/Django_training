from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Одежда для кукол", 'url_name': 'clothes'},
        {'title': "Обувь для кукол", 'url_name': 'footwear'},
        {'title': "Хвастики", 'url_name': 'photo'},
        {'title': "Войти", 'url_name': 'login'}
        ]
typ_clothing = [
    {'id': 1, 'title': 'Свитшот для куклы Paola Reina', 'content': 'Характеристики и описание', 'аvailability': True},
    {'id': 2, 'title': 'Блузка для куклы Paola Reina', 'content': 'Характеристики и описание', 'аvailability': True},
    {'id': 3, 'title': 'Наушники для кукол', 'content': 'Характеристики и описание', 'аvailability': True}
]

typ_footwear = [
    {'id': 1, 'title': 'Ботинки для куклы Paola Reina', 'content': 'Характеристики и описание', 'аvailability': True},
    {'id': 2, 'title': 'Мокасины для Paola Reina 32 см', 'content': 'Характеристики и описание', 'аvailability': True},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'dolls/index.html', data)


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'dolls/index.html', data)


def clothes(request):
    data = {
        'title': 'Одежда для кукол',
        'typ_clothing': typ_clothing,
    }
    return render(request, 'dolls/clothes.html', data)


def footwear(request):
    data = {
        'title': 'Обувь для кукол',
        'typ_footwear': typ_footwear,
    }
    return render(request, 'dolls/footwear.html', data)


def photo(request):
    return HttpResponse(f"Хвастики")


def login(request):
    return HttpResponse(f"Войти")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
