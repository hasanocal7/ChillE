import typing
import strawberry

@strawberry.type
class AccountType:
    username: str
    email: str
    password: str
    fullname: str
    phonenumber: str
    address: str