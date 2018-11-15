from django.shortcuts import render
from .models import Cart


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj

def carts_home(request):
    # cart_id = request.session.get("cart_id", None)
    # if cart_id is None:
    #     request.session['cart_id'] = cart_obj.id
    # else:
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        cart_obj.first()
    else:
        cart_obj = Cart.objects.new(user=None)
    return render(request, "carts/index.html", {})
