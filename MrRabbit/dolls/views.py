from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.template.loader import render_to_string

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Одежда для кукол", 'url_name': 'clothes'},
        {'title': "Обувь для кукол", 'url_name': 'footwear'},
        {'title': "Хвастики", 'url_name': 'photo'},
        {'title': "Войти", 'url_name': 'login'}
        ]

typ_clothing = [
    {'id': 1, 'title': 'Свитшот для куклы Paola Reina', 'typ': 'Свитшоты', 'content': 'Характеристики и описание',
     'аvailability': True},
    {'id': 2, 'title': 'Блузка для куклы Paola Reina', 'typ': 'Блузки', 'content': 'Характеристики и описание',
     'аvailability': True},
    {'id': 3, 'title': 'Наушники для кукол', 'typ': 'Наушники', 'content': 'Характеристики и описание',
     'аvailability': True}
]

typ_footwear = [
    {'id': 1, 'title': 'Ботинки для куклы Paola Reina', 'content': 'Характеристики и описание', 'аvailability': True},
    {'id': 2, 'title': 'Мокасины для Paola Reina 32 см', 'content': 'Характеристики и описание', 'аvailability': True},
]

menu_selection_clothes = [
    {'title': "Верхняя одежда", 'typ': "Верхняя одежда"},
    {'title': "Свитшоты", 'typ': "Свитшоты"},
    {'title': "Блузки", 'typ': "Блузки"},
    {'title': "Юбки", 'typ': "Юбки"},
    {'title': "Джинсы", 'typ': "Джинсы"},
    {'title': "Наушники", 'typ': "Наушники"}
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu
    }
    return render(request, 'dolls/index.html', data)


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu
    }
    return render(request, 'dolls/about.html', data)


def clothes(request):
    data = {
        'menu_selection_clothes': menu_selection_clothes,
        'title': 'Одежда для кукол',
        'menu': menu,
        'typ_clothing': typ_clothing
    }
    return render(request, 'dolls/clothes.html', data)


def footwear(request):
    data = {
        'title': 'Обувь для кукол',
        'menu': menu,
        'typ_footwear': typ_footwear
    }
    return render(request, 'dolls/footwear.html', data)


def photo(request):
    data = {
        'title': 'Хвастики',
        'menu': menu,
    }
    return render(request, 'dolls/photo.html', data)


def login(request):
    return HttpResponse(f"Войти")


def show_post_clothes(request, post_id):
    return render(request, f'dolls/characteristics_description/clothes/{post_id}.html',
                  {'title': 'Характеристики и описание', 'menu': menu})


def show_post_footwear(request, post_id):
    return render(request, f'dolls/characteristics_description/footwear/{post_id}.html',
                  {'title': 'Характеристики и описание', 'menu': menu})


def show_selection_clothes(request):
    data = {
        'menu_selection_clothes': menu_selection_clothes,
        'menu': menu,
        'typ_clothing': typ_clothing
    }
    return render(request, f'dolls/selection_clothes.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def server_error(request):
    return HttpResponseServerError("<h1>На сервере произошла неожиданная ошибка. Невозможно выполнить запрос. </h1>")
