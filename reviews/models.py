from django.db import models
from users.models import CustomUser
from products.models import Product

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reviews"
