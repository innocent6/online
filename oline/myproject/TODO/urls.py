from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListTodo.as_views()),
    path('<int:pk>/',views.DetailTodo.as_views()),
    
]
