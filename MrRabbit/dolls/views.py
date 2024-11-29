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


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'dolls/index.html', data)


def about(request):
    return HttpResponse(f"О сайте")


def clothes(request):
    data = {
        'title': 'Одежда для кукол',
        'typ_clothing': typ_clothing,
    }
    return render(request, 'dolls/clothes.html', data)


def footwear(request):
    return HttpResponse(f"Обувь для кукол")


def photo(request):
    return HttpResponse(f"Хвастики")


def login(request):
    return HttpResponse(f"Войти")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
