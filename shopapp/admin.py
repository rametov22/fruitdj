from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ShopModel)
admin.site.register(AddCart)
admin.site.register(FeaturedModel)
admin.site.register(ShopBanner)
admin.site.register(Category)
admin.site.register(ShippingMethod)
admin.site.register(PaymentMethod)
admin.site.register(Order)