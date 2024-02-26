import strawberry_django
from categories.types import SubCategoryType
from tags.types import TagType
from strawberry import auto
from .models import Product
@strawberry_django.type(Product)
class ProductType:
    title: auto
    description: auto
    price: auto
    category: "SubCategoryType"
    stock_quantity: auto
    image_url: auto
    tags: list[TagType]
    created_at: auto
    updated_at: auto
