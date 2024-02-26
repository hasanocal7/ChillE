import strawberry_django
from strawberry import auto
from .models import Invoice
@strawberry_django.type(Invoice)
class InvoiceType:
    order = "OrderType"
    invoice_number: auto
    invoice_date: auto
    invoice_amount: auto