from django.contrib import admin
from .models import Category, ProductCategory, SubCategory, ProductSubCategory, Vendor, ProductVendor
# Register your models here.

admin.site.register(Category)
admin.site.register(ProductCategory)
admin.site.register(SubCategory)
admin.site.register(ProductSubCategory)
admin.site.register(Vendor)
admin.site.register(ProductVendor)