from django.urls import path 
from .views import  indexPageView, addTodo, delete, userGreetingView, getItemsVulnerable

urlpatterns = [
  path('', indexPageView, name='index'),
  path('greeting/', userGreetingView, name='greeting'),
  path('add/', addTodo, name='add'),
  path('delete/', delete, name='delete'),
  path('getItemsVulnerable/', getItemsVulnerable, name='getItemsVulnerable')
]