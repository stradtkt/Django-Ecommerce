from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product


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