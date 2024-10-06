# backend/app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about'),
    path('team/', views.team, name='team'),
    path('resources/', views.resources, name='resources'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact_us, name='contact'),
]
