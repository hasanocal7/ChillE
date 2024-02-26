import strawberry_django
from strawberry import auto
from .models import Account

@strawberry_django.type(Account)
class AccountType:
    username: auto
    email: auto
    password: auto
    fullname: auto
    phonenumber: auto
    address: auto