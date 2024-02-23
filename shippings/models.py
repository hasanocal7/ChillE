from django.db import models
from orders.models import Order

class Shipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipping_company = models.CharField(max_length=255)
    shipping_tracking_code = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.order.order_date} - {self.shipping_company}"
