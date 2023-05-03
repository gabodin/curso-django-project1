from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('recipes/<int:id>/', views.recipe)
]
