import typing
import strawberry
from users.types import AccountType
from datetime import datetime

@strawberry.type
class OrderType:
    user: "AccountType"
    order_date: datetime
    delivery_address: str
    delivery_phone_number: str
    shipping_status: str
