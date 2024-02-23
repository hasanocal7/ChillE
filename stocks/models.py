from django.db import models
from products.models import Product
from warehouses.models import Warehouse

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    min_quantity_level = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.product.title} - {self.quantity}"