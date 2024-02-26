import strawberry_django
from .models import Shipping
from orders.types import OrderType
from strawberry import auto

@strawberry_django.type(Shipping)
class ShippingType:
    order: "OrderType"
    shipping_company: auto
    shipping_tracking_code: auto