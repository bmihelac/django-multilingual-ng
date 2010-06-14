from django.db import models

import multilingual


class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Translation(multilingual.Translation):
        name = models.CharField(max_length=250)


class ProductVariant(models.Model):
    product = models.ForeignKey(Product)

    class Translation(multilingual.Translation):
        color = models.CharField(max_length=80)