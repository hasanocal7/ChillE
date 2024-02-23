from django.db import models
from orders.models import Order

PAYMENT_TYPE = {
    'Credit Card': 'Credit Card',
    'Wire Transfer/EFT': 'Wire Transfer/EFT',
    'Cash on Delivery': 'Cash on Delivery'
}

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length = 255, choices=PAYMENT_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    process_ID = models.CharField(max_length=255, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.order.order_date} - {self.payment_date}"