from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
# Create your views here.
from .models import Todo
from rest_framework.response import Response
from .serializer import TodoSerializer
from rest_framework.views import APIView


class list_todos(APIView):
    def get(self, request, format=None):
        todos = Todo.objects.all()
        print(todos)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


def insert_todo_item(request: HttpRequest):
    content = request.POST['content']
    todo = Todo(content)
    todo.save()
    return HttpResponse(todo)
