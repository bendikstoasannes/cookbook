from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='overskrift')
    ingredients = models.TextField(default="", verbose_name='ingredienser')
    instructions = models.TextField(default="", verbose_name='framgangsmate')

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
