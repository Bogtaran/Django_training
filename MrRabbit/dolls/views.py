from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from dolls.models import Typ_clothing, Menu_selection_clothes

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Одежда для кукол", 'url_name': 'clothes'},
        {'title': "Обувь для кукол", 'url_name': 'footwear'},
        {'title': "Хвастики", 'url_name': 'photo'},
        {'title': "Войти", 'url_name': 'login'}
        ]

typ_footwear = [
    {'id': 1, 'title': 'Ботинки для куклы Paola Reina', 'typ': 'Ботинки', 'content': 'Характеристики и описание',
     'availability': True},
    {'id': 2, 'title': 'Мокасины для Paola Reina 32 см', 'typ': 'Мокасины', 'content': 'Характеристики и описание',
     'availability': True},
]

menu_selection_footwear = [
    {'typ': "Ботинки"},
    {'typ': "Мокасины"},
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
    Typ_clot = Typ_clothing.availability.all()
    menu_selection_clothes = Menu_selection_clothes.objects.all()

    data = {
        'menu_selection_clothes': menu_selection_clothes,
        'title': 'Одежда для кукол',
        'menu': menu,
        'typ_clothing': Typ_clot
    }
    return render(request, 'dolls/clothes.html', data)


def footwear(request):
    data = {
        'title': 'Обувь для кукол',
        'menu': menu,
        'typ_footwear': typ_footwear,
        'menu_selection_footwear': menu_selection_footwear
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


def show_post_clothes(request, post_slug):
    post = get_object_or_404(Typ_clothing, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post
    }
    return render(request, f'dolls/characteristics_description/clothes/clothes.html', data)


def show_post_footwear(request, post_id):
    return render(request, f'dolls/characteristics_description/footwear/{post_id}.html',
                  {'title': 'Характеристики и описание', 'menu': menu})


def show_selection_clothes(request, cloth_type):
    Typ_clot = Typ_clothing.availability.filter(typ=cloth_type)
    menu_selection_clothes = Menu_selection_clothes.objects.all()


    data = {
        'menu_selection_clothes': menu_selection_clothes,
        'menu': menu,
        'typ_clothing': Typ_clot,
        'title': cloth_type,
    }
    return render(request, f'dolls/selection_clothes.html', data)


def show_selection_footwear(request, foot_type):
    data = {
        'menu_selection_footwear': menu_selection_footwear,
        'menu': menu,
        'typ_footwear': typ_footwear,
        'title': foot_type,
        'foot_type': foot_type
    }
    return render(request, f'dolls/selection_footwear.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def server_error(request):
    return HttpResponseServerError("<h1>На сервере произошла неожиданная ошибка. Невозможно выполнить запрос. </h1>")
