from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения dolls')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id:{cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id:{cat_slug}</p>")
