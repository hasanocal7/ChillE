from strawberry_django.optimizer import DjangoOptimizerExtension
import strawberry
import strawberry_django
from products.resolvers import get_all_products, get_product
from strawberry_django import mutations, NodeInput
from products.types import ProductType, ProductInput, ProductRequiredPartialInput
from users.types import UserType, UserInput
from gqlauth.user.queries import UserQueries
from gqlauth.user import arg_mutations as auth_mutations

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
class Query(UserQueries):
    products: list[ProductType] = strawberry_django.field(resolver=get_all_products, pagination=True)
    product: ProductType = strawberry_django.field(resolver=get_product)

@strawberry.type
class Mutation:
    verify_token = auth_mutations.VerifyToken.field
    update_account = auth_mutations.UpdateAccount.field
    archive_account = auth_mutations.ArchiveAccount.field
    delete_account = auth_mutations.DeleteAccount.field
    password_change = auth_mutations.PasswordChange.field
    token_auth = auth_mutations.ObtainJSONWebToken.field
    register = auth_mutations.Register.field
    verify_account = auth_mutations.VerifyAccount.field
    resend_activation_email = auth_mutations.ResendActivationEmail.field
    send_password_reset_email = auth_mutations.SendPasswordResetEmail.field
    password_reset = auth_mutations.PasswordReset.field
    password_set = auth_mutations.PasswordSet.field
    refresh_token = auth_mutations.RefreshToken.field
    revoke_token = auth_mutations.RevokeToken.field

    create_product: ProductType = mutations.create(ProductInput)
    update_product: ProductType = mutations.update(ProductRequiredPartialInput)
    delete_product: ProductType = mutations.delete(NodeInput)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
    DjangoOptimizerExtension
])