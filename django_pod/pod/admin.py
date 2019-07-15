from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import SKU, Brand, Retailer, PurchaseOrder

admin.site.register(SKU)
admin.site.register(Brand)
admin.site.register(Retailer)
admin.site.register(PurchaseOrder)