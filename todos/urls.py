from django.contrib import admin
from django.urls import path, include

from .views import list_todos, insert_todo_item

urlpatterns = [
    path('list/', list_todos.as_view()),
    path('insert_todo/', insert_todo_item),
]
