from django.db import models

class Account(models.Model):
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    fullname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return self.username