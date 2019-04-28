from django.urls import path
from . import views
from django.contrib.auth import views as django_views

app_name = "book"

login_urls = [
    path('accounts/login/', django_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', django_views.LogoutView.as_view(next_page='/'), name='logout')
]

recipe_urls = [
    path('', views.index, name='index'),
    path('oppskrifter/', views.recipe_list, name='recipe_list'),
    path('oppskrifter/<int:page>', views.recipe_list, name='detail'),
    path('oppskrifter/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('oppskrifter/ny', views.recipe_new, name='recipe_new'),
    path('oppskrifter/<int:pk>/rediger', views.recipe_edit, name='recipe_edit'),
    path('oppskrifter/<int:pk>/slett', views.recipe_remove, name='recipe_remove'),
    path('oppskrifter/<int:pk>/kommenter/', views.add_comment_to_recipe, name='add_comment_to_recipe'),
    path('sok/', views.search_recipe, name='search_recipe')
]

category_urls = [
    path('kategorier', views.category_list, name="category_list"),
    path('kategorier/ny', views.create_category, name='create_category'),
    path('category-autocomplete/', views.CategoryAutocomplete.as_view(), name='category-autocomplete')
]

urlpatterns = recipe_urls + category_urls + login_urls
