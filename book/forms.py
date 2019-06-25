from django import forms
from .models import Recipe, Comment, Category


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
            'categories': forms.CheckboxSelectMultiple()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        labels = {'author': 'Forfatter',
                  'text': 'Kommentartekst'}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
