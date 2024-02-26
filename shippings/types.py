import typing
import strawberry
from orders.types import OrderType

@strawberry.type
class ShippingType:
    order: "OrderType"
    shipping_company: str
    shipping_tracking_code: str