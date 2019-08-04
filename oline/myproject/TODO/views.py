from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import Todoserializer

# Create your views here.
class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializer
    
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.object.all()
    serializer_class = Todoserializer
        
    
    
