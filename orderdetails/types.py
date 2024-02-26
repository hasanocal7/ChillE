import strawberry_django
from strawberry import auto
from .models import OrderDetail
from orders.types import OrderType
from products.types import ProductType

@strawberry_django.type(OrderDetail)
class OrderDetailType:
    order: "OrderType"
    product: "ProductType"
    quantity: auto
    price: auto