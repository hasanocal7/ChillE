from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "categories"

    def __str__(self) -> str:
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = "subcategories"
    
    def __str__(self) -> str:
        return self.name
