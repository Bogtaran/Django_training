from django.db import models

class Typ_clothing(models.Model):
    title = models.CharField(max_length=150)
    typ = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title

