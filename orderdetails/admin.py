from django.contrib import admin
from .models import OrderDetail

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin): pass
