from django import forms
from dal import autocomplete
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'instructions', 'categories')
        labels = {'title': 'Tittel',
                  'ingredients': 'Ingredienser',
                  'instructions': 'Fremgangsmåte',
                  'categories': 'Kategorier'
                  }
        widgets = {
            'categories': autocomplete.ModelSelect2Multiple(url='book:category-autocomplete')
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        labels = {'author': 'Forfatter',
                  'text': 'Kommentartekst'}
