from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    description = models.TextField(max_length=1000)
    discount_price = models.FloatField(default=0)
    category = models.CharField(max_length=200)
    image = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
