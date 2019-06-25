from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='kategori')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='overskrift')
    ingredients = RichTextField(verbose_name='ingredienser', config_name='default')
    instructions = RichTextField(default="", verbose_name='framgangsmate')
    categories = models.ManyToManyField(Category, default=None, verbose_name='kategori')

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Comment(models.Model):
    recipe = models.ForeignKey('book.Recipe', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now())

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

