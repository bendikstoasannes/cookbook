from django import forms
from django.db import models
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
                'rows': 8}),

            'categories': forms.CheckboxSelectMultiple()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        labels = {'author': 'Forfatter',
                  'text': 'Kommentartekst'}
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Skriv inn navn...'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Skriv inn kommentartekst...'
            })
        }
