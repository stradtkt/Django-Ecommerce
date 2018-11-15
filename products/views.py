from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product
from carts.models import Cart

class ProductDetailView(DetailView):
    template_name = "products/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product does not exist")
        return instance
    

def product_detail_view(request, pk=None, *args, **kwargs):
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     raise Http404("Product, doesn't exist")
    # except:
    #     print("Message")
    # qs = Product.objects.get(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http("Product doesn't exist")

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product, doesn't exist")

    context = {
        "object": instance
    }
    return render(request, "products/detail.html", context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context
    
    def get_obj(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("There was an error")
        return instance