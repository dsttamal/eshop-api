from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField(default=0)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')

    def __str__(self):
        return self.product.name
    
    class Meta:
        db_table = "images"
