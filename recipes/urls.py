from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='recipe')
]
