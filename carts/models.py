from decimal import Decimal
from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed
User = settings.AUTH_USER_MODEL



class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = self.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user_obj
        return self.model.objects.create(user=user_obj)

class Cart(models.Model):
    user = models.ForeignKey(User, related_name="buyer", null=True, blank=True)
    products = models.ManyToManyField(Product, related_name="products")
    total = models.DecimalField(decimal_places=2, max_digits=20)
    subtotal = models.DecimalField(decimal_places=2, max_digits=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CartManager()
    def __str__(self):
        return str(self.id)


def m2m_changed_cart_reciever(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for p in products:
            total += p.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()

m2m_changed.connect(m2m_changed_cart_reciever, sender=Cart.products.through)

def pre_save_cart_reciever(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal) * Decimal(1.08)
    else:
        instance.total = 0.00

pre_save.connect(pre_save_cart_reciever, sender=Cart)