from django.contrib import admin


# Register your models here.
from .models import Customer, Category, Cart, Product, CartItem
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(CartItem)
