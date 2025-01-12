from django.db import models
from django.urls import reverse


class AvailabilityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_availability=1)


class Typ_clothing(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    typ = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    is_availability = models.BooleanField(default=True)

    objects = models.Manager()
    availability = AvailabilityManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_clothes', kwargs={'post_slug': self.slug})
