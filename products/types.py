import strawberry_django
from categories.types import SubCategoryType
from tags.types import TagType
from strawberry import auto
from .models import Product
from typing import List
@strawberry_django.type(Product)
class ProductType:
    id: auto
    title: auto
    description: auto
    price: auto
    category: "SubCategoryType"
    stock_quantity: auto
    image_url: auto
    tags: List[TagType]
    created_at: auto
    updated_at: auto

@strawberry_django.input(Product)
class ProductInput:
    title: auto
    description: auto
    price: auto
    category: "SubCategoryType"
    stock_quantity: auto
    image_url: auto
    tags: List[TagType]

@strawberry_django.input(Product, partial=True)
class ProductRequiredPartialInput(ProductInput):
    title: str
    description: str
    price: float
    category: "SubCategoryType"
    stock_quantity: int
    image_url: auto
    tags: List[TagType]