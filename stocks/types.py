from .models import Stock
from strawberry import auto
import strawberry_django
from products.types import ProductType
from warehouses.types import WarehouseType

@strawberry_django.type(Stock)
class StockType:
    product: "ProductType"
    quantity: auto
    min_quantity_level: auto
    warehouse: "WarehouseType"