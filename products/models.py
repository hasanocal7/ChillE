from django.db import models
from categories.models import SubCategory
from tags.models import Tag

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, default=None)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.ImageField(upload_to="products/", default=None)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products" 
    
    def __str__(self) -> str:
        return self.title