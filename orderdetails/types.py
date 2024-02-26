import typing
import strawberry
from orders.types import OrderType
from products.types import ProductType

@strawberry.type
class OrderDetailType:
    order: "OrderType"
    product: "ProductType"
    quantity: int
    price: float