from django.contrib import admin
from django.urls import path, include
from .views import home, about
urlpatterns = [
    path('', home, name='blog_home'),
    path('about/', about, name='blog_about'),


]
