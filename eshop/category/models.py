from django.db import models
from products.models import Product
# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, default='')

    @property
    def url_to_get_products(self):
        return f'product/category/{self.slug}/'

    def __str__(self):
        return self.url_to_get_products

    class Meta:
        db_table = "categories"

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name

    class Meta:
        db_table = "product_category"

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, default='')

    def __str__(self):
        return self.name
    class Meta:
        db_table = "sub_categories"

class ProductSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.subCategory.name

    class Meta:
        db_table = "product_sub_category"

class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, default='')

    def __str__(self):
        return self.name
    class Meta:
        db_table = "Vendor"

class ProductVendor(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.Vendor.name

    class Meta:
        db_table = "product_Vendor"
