from django.http import HttpResponse
from django.shortcuts import render

from recipes.models import Category, Recipe
from utils.recipes.factory import make_recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')

    return render(request, 'recipes/pages/home.html', status=200, context={
        'recipes': recipes,
    })


def recipes_by_category(request, category_id):
    recipes_by_category = Recipe.objects.filter(
        category__id=category_id).order_by('-id')

    return render(request, 'recipes/pages/home.html', status=200, context={
        'recipes': recipes_by_category,
    })


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)

    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        'recipe': recipe,
        'is_detail_page': True
    })
