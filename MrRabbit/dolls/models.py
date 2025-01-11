from django.db import models
from django.urls import reverse


class Typ_clothing(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    typ = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_clothes', kwargs={'post_slug': self.slug})
