from django.contrib import admin
from django.urls import path, include
from hostinfo import views

urlpatterns = [
    path('', views.hostsinfo, name='hostsinfo'),
    path('index/', views.hostsinfo, name='hostsinfo'),
    path('search/', views.search, name='search'),
    path('about/', views.aboutme, name='aboutme'),
]
