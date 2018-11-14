from django.http import HttpResponse
from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'home_page.html', {})

def about_page(request):
    return render(request, 'about_page.html', {})

def contact_page(request):
    return render(request, 'contact_page.html', {})