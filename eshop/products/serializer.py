from rest_framework import serializers
from .models import Product, Image
from category.models import ProductCategory, ProductSubCategory, ProductVendor
from category.serializer import ProductCategorySerializer, ProductSubCategorySerializer, ProductVendorSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', )

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()
    Vendor = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'discount',
                  'stock', 'images', 'category', 'subcategory', 'Vendor')

    def get_images(self, obj):
        images = Image.objects.filter(product=obj)
        serializer = ImageSerializer(images, many=True)
        return serializer.data

    def get_category(self, obj):
        productCategory = ProductCategory.objects.filter(product=obj)
        serializer = ProductCategorySerializer(productCategory, many=True)
        return serializer.data

    def get_subcategory(self, obj):
        productsubcategory = ProductSubCategory.objects.filter(product=obj)
        serializer = ProductSubCategorySerializer(
            productsubcategory, many=True)
        return serializer.data

    def get_Vendor(self, obj):
        productVendor = ProductVendor.objects.filter(product=obj)
        serializer = ProductVendorSerializer(productVendor, many=True)
        return serializer.data
