import strawberry_django
from users.types import UserType
from .models import Order
from strawberry import auto
@strawberry_django.type(Order)
class OrderType:
    user: "UserType"
    order_date: auto
    delivery_address: auto
    delivery_phone_number: auto
    shipping_status: auto
