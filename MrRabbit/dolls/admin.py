from django.contrib import admin
from .models import Typ_clothing, Menu_selection_clothes


@admin.register(Typ_clothing)
class Typ_clothingAdmin(admin.ModelAdmin):
    list_display = ('title', 'selection_clothes', 'is_availability')
    list_editable = ['is_availability']
    list_per_page = 7

@admin.register(Menu_selection_clothes)
class Menu_selection_clothesAdmin(admin.ModelAdmin):
    list_display = ('typ',)
    list_per_page = 8

