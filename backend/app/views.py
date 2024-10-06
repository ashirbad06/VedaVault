# backend/app/views.py

from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return JsonResponse({'message': 'About Us Page'})

def team(request):
    return JsonResponse({'message': 'Team Page'})

def resources(request):
    return JsonResponse({'message': 'Resources Page'})

def services(request):
    return JsonResponse({'message': 'Services Page'})

def contact_us(request):
    return JsonResponse({'message': 'Contact Us Page'})
