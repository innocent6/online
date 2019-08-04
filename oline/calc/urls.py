from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

from . import views

urlpatterns = [
    path('employees', views.employees, name ='employees'),
   
 ]