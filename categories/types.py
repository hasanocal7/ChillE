import strawberry_django 
from strawberry import auto
from .models import SubCategory, Category

@strawberry_django.type(Category)
class CategoryType: 
    id: auto
    name: auto

@strawberry_django.type(SubCategory)
class SubCategoryType: 
    id: auto
    name: auto
    categories: list[CategoryType]