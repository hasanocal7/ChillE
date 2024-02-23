from django.contrib import admin
from .models import Shipping

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin): pass
