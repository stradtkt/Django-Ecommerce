from django.shortcuts import render
from .models import Cart
from products.models import Product

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj

def carts_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    
    context = {
        "cart": cart_obj
    }
    return render(request, "carts/index.html", context)

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user product is gone")
            return redirect("cart:home")
        product_obj = Product.objects.get(id=product_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        # return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")