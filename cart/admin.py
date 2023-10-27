from django.contrib import admin
from .models import Cart, Wishlist, CartItem

admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(CartItem)
