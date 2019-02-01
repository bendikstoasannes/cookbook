from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from django.utils import timezone
from .forms import RecipeForm, CommentForm

# Create your views here.

def index(request):
    recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    count = recipes.count()
    if len(recipes) <= 5:
        return render(request, 'book/index.html', {'recipes': recipes, 'count': count})
    else:
        return render(request, 'book/index.html', {'recipes': recipes[:5], 'count': count})


def recipe_list(request):
    recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('title')
    return render(request, 'book/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'book/recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'book/recipe_edit.html', {'form': form})

@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.save()
            form.save_m2m()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'book/recipe_edit.html', {'form': form, 'recipe': recipe})

@login_required
def recipe_remove(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')

def add_comment_to_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = CommentForm()
    return render(request, 'book/comment_to_recipe.html', {'form': form})
