from django.db import models
from products.models import Product
# Create your models here.
class orderProduct(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    order_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_delivered = models.BooleanField(default=False)

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = "orders"