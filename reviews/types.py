from .models import Review
import strawberry_django
from strawberry import auto
from users.types import UserType
from products.types import ProductType

@strawberry_django.type(Review)
class ReviewType:
    user: "UserType"
    rating: auto
    comment: auto
    product: "ProductType"
    created_at: auto