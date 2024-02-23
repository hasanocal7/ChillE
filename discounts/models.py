from django.db import models

class DiscountCoupon(models.Model):
    code = models.CharField(max_length=255, unique=True)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    min_order_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.code} - {self.discount_rate}%"