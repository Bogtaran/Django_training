from django.db import models
from django.urls import reverse


class AvailabilityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_availability=Typ_clothing.Status.AVAILABILITY)


class Typ_clothing(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Недоступно'
        AVAILABILITY = 1, 'Доступно'

    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    content = models.TextField(blank=True, verbose_name='Описание')
    is_availability = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.DRAFT, verbose_name='Наличие')
    selection_clothes = models.ForeignKey('Menu_selection_clothes', on_delete=models.PROTECT,
                                          related_name='typ_clot', verbose_name='Вид одежды')

    objects = models.Manager()
    availability = AvailabilityManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_clothes', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Одежда для кукол"
        verbose_name_plural = "Одежда для кукол"


class Menu_selection_clothes(models.Model):
    typ = models.CharField(max_length=100, db_index=True, verbose_name='Вид')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.typ

    def get_absolute_url(self):
        return reverse('selection_clothes', kwargs={'cloth_type': self.slug})

    class Meta:
        verbose_name = "Вид одежды"
        verbose_name_plural = "Вид одежды"
