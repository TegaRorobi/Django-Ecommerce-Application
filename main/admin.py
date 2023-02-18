from django.contrib import admin


# Register your models here.
from .models import *
admin.site.register(User)
admin.site.register(Category)
admin.site.register(BuyerProfile)
admin.site.register(SellerProfile)
admin.site.register(Product)
