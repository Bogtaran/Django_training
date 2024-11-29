from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    # t = render_to_string('dolls/index.html')
    # return HttpResponse(t)
    return render(request, 'dolls/index.html')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id:{cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id:{cat_slug}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def clothes(request):
    return render(request, 'dolls/clothes.html')