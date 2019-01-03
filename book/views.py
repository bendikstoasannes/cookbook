from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.utils import timezone

# Create your views here.

def recipe_list(request):
    recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'book/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'book/recipe_detail.html', {'recipe': recipe})
