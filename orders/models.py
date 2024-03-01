from django.db import models
from users.models import CustomUser

SHIPPING_STATUS = (("SHIPPING WAITING","SHIPPING WAITING"),
                   ("SHIPPED","SHIPPED"),
                   ("DELIVERED","DELIVERED"))

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()
    delivery_phone_number = models.CharField(max_length=10, blank=True)
    shipping_status = models.CharField(max_length=255, choices=SHIPPING_STATUS) 

    def __str__(self) -> str:
        return f"{self.order_date} - {self.user.username}"