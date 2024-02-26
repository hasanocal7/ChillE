import typing
import strawberry

@strawberry.type
class WarehouseType:
    name: str
    address: str