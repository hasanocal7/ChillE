from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name