from django.db import models
from django.urls import reverse


class AvailabilityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_availability=Typ_clothing.Status.AVAILABILITY)


class Typ_clothing(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Недоступно'
        AVAILABILITY = 1, 'Доступно'

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    typ = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    is_availability = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    selection_clothes = models.ForeignKey('Menu_selection_clothes', on_delete=models.PROTECT)

    objects = models.Manager()
    availability = AvailabilityManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_clothes', kwargs={'post_slug': self.slug})


class Menu_selection_clothes(models.Model):
    typ = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.typ

    def get_absolute_url(self):
        return reverse('selection_clothes', kwargs={'cloth_type': self.slug})


menu_selection_clothes = [
    {'typ': "Верхняя одежда"},
    {'typ': "Свитшоты"},
    {'typ': "Блузки"},
    {'typ': "Юбки"},
    {'typ': "Джинсы"},
    {'typ': "Наушники"}
]
