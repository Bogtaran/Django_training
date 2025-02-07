from django.contrib import admin
from .models import Typ_clothing, Menu_selection_clothes


@admin.register(Typ_clothing)
class Typ_clothingAdmin(admin.ModelAdmin):
    list_display = ('title', 'selection_clothes', 'is_availability', 'slug')
    list_editable = ['is_availability', 'slug']
    search_fields = ['title', 'selection_clothes__typ']
    list_filter = ['selection_clothes__typ', 'is_availability']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 7


@admin.register(Menu_selection_clothes)
class Menu_selection_clothesAdmin(admin.ModelAdmin):
    list_display = ('typ',)
    list_per_page = 8
