import strawberry_django
from .models import DiscountCoupon
from strawberry import auto

@strawberry_django.type(DiscountCoupon)
class DiscountCouponType:
    code: auto
    discount_rate: auto
    start_date: auto
    end_date: auto
    min_order_amount: auto