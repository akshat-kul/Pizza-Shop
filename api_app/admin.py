from django.contrib import admin

from .models import CartItem, PizzaItem, ToppingItem

admin.site.register(CartItem)
admin.site.register(PizzaItem)
admin.site.register(ToppingItem)
