import typing
import strawberry
from categories.types import SubCategoryType
from tags.types import TagType
from datetime import datetime

@strawberry.type
class ProductType:
    title: str
    description: str
    price: float
    category: "SubCategoryType"
    stock_quantity: int
    image_url: str
    tags: ["TagType"]
    created_at: datetime
    updated_at: datetime
