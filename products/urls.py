from django.conf.urls import url
from . import views

urlpatterns = [
    #how you implement a slug
    url(r'^(?P<slug>[\w-]+)/$', views.ProductDetailSlugView.as_view())
]
