from django.contrib import admin
from .models import Warehouse

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin): pass
