from django.db import models
from orders.models import Order

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=255)
    invoice_date = models.DateTimeField(auto_now_add=True)
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.order.order_date} - {self.invoice_number}"