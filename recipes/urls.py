from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('recipes/category/<int:category_id>',
         views.recipes_by_category, name='category'),
    path('recipes/<int:id>/', views.recipe, name='recipe')
]
