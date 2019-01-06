from django import forms
from django.db import models
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'instructions',)
        labels = {'title': 'Tittel',
                  'ingredients': 'Ingredienser',
                  'instructions': 'Fremgangsmåte'
                  }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Skriv inn tittel...'}),

            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Skriv inn ingredienser...',
                'rows': 8}),

            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Skriv inn fremgangsmåte...',
                'rows': 8})
        }
