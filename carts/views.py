from django.shortcuts import render
from .models import Cart


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj

def carts_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    
    context = {
        "cart": cart_obj
    }
    return render(request, "carts/index.html", context)
