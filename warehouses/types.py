from strawberry import auto
import strawberry_django
from .models import Warehouse

@strawberry_django.type(Warehouse)
class WarehouseType:
    name: auto
    address: auto