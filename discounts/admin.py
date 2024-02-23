from django.contrib import admin
from .models import DiscountCoupon

@admin.register(DiscountCoupon)
class DiscountCouponAdmin(admin.ModelAdmin): pass
