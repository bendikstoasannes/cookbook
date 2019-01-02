from django.shortcuts import render
from .models import Recipe
from django.utils import timezone

# Create your views here.

def recipe_list(request):
    recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'book/recipe_list.html', {'recipes': recipes})
