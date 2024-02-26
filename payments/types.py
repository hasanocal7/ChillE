import strawberry_django
from orders.types import OrderType
from .models import Payment
from strawberry import auto

@strawberry_django.type(Payment)
class PaymentType:
    order: "OrderType"
    payment_type: auto
    amount: auto
    process_ID: auto
    payment_date: auto