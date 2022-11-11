from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва міста")
    slug = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = "Назви міст"
        verbose_name_plural = "Назва міста"

    def __str__(self):
        return self.name

