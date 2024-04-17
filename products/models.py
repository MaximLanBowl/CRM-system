import datetime
import time

from django.db import models
from django.urls import reverse


class Product(models.Model):

    class Meta:
        ordering = ["name", "price"]
        verbose_name = "product"
        verbose_name_plural = "products"

    objects = None
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:details", kwargs={"pk": self.pk})




