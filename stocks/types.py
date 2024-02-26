import typing
import strawberry
from products.types import ProductType
from warehouses.types import WarehouseType

@strawberry.type
class StockType:
    product: "ProductType"
    quantity: int
    min_quantity_level: int
    warehouse: "WarehouseType"