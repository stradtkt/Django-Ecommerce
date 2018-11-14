from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm

def home_page(request):
    return render(request, 'home_page.html', {})

def about_page(request):
    return render(request, 'about_page.html', {})

def contact_page(request):
    contact = ContactForm(request.POST or None)
    context = {
        "form": contact
    }
    if contact.is_valid():
        print(contact.clean_data)

    return render(request, 'contact_page.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #context['form'] = LoginForm()
            print(request.user.is_authenticated())
            return redirect('/login')
        else:
            print("Error")

    return render(request, 'auth/login.html', context)

def register_page(request):
    return render(request, 'auth/register.html', {})