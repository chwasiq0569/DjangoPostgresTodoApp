from django.contrib import admin
from django.urls import path, include

from .views import list_todos

urlpatterns = [
    path('list/', list_todos),
]
