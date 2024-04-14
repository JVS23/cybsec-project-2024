from django.urls import path 
from .views import  indexPageView, addTodo, delete #, todoView

urlpatterns = [
  path('', indexPageView, name='index'),
  #path('todos/', todoView, name='todos'),
  path('add/', addTodo, name='add'),
  path('delete/', delete, name='delete'),
]