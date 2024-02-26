import typing
import strawberry

@strawberry.type
class CategoryType:
    name: str

@strawberry.type
class SubCategoryType:
    name: str
    categories: typing.List["CategoryType"]