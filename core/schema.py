from strawberry_django.optimizer import DjangoOptimizerExtension
import strawberry
import strawberry_django
from products.resolvers import get_all_products, get_product
from strawberry_django import mutations, NodeInput
from products.types import ProductType, ProductInput, ProductRequiredPartialInput

""" 
query {
  products(pagination: { offset: 0, limit: 2 }) {
    title
    description
    price
  }


  {
  products{
  	title
    description
    price
    category{
      name
    }
    stockQuantity
    imageUrl{name}
    tags{
      name
    }
  }
}
} """

@strawberry.type
class Query:
    products: list[ProductType] = strawberry_django.field(resolver=get_all_products, pagination=True)
    product: ProductType = strawberry_django.field(resolver=get_product)

@strawberry.type
class Mutation:
    create_product: ProductType = mutations.create(ProductInput)
    update_product: ProductType = mutations.update(ProductRequiredPartialInput)
    delete_product: ProductType = mutations.delete(NodeInput)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
    DjangoOptimizerExtension
])