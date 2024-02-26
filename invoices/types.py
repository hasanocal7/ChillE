import typing
import strawberry
from orders.types import OrderType
from datetime import datetime

@strawberry.type
class InvoiceType:
    order = "OrderType"
    invoice_number: str
    invoice_date: datetime
    invoice_amount: float