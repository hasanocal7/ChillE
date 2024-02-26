import typing
import strawberry
from orders.types import OrderType
from datetime import datetime

@strawberry.type
class PaymentType:
    order: "OrderType"
    payment_type: str
    amount: float
    process_ID: str
    payment_date: datetime