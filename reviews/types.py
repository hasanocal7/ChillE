import typing
import strawberry
from products.types import ProductType
from users.types import AccountType
from datetime import datetime

@strawberry.type
class ReviewType:
    user: "AccountType"
    rating: int
    comment: str
    product: "ProductType"
    created_at: datetime