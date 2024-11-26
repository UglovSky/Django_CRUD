from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    price = models.FloatField(verbose_name="Price")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return f'{self.name}: {self.description}({self.price}руб)'

