from django.contrib import admin

from .models import PizzaItem, ToppingItem

admin.site.register(PizzaItem)
admin.site.register(ToppingItem)
