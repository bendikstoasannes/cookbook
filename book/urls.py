from django.urls import path
from . import views
from django.contrib.auth import views as django_views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', django_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', django_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('recipe_list', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/new', views.recipe_new, name='recipe_new'),
    path('recipe/<int:pk>/edit', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/remove', views.recipe_remove, name='recipe_remove'),
    path('recipe/<int:pk>/comment/', views.add_comment_to_recipe, name='add_comment_to_recipe'),
    path('search/', views.search_recipe, name='search_recipe')
]
