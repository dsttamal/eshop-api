from django.db import models
from products.models import Product
# Create your models here.

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = "cart"
# Create your models here.
