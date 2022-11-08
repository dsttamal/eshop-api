from rest_framework import serializers
from .models import ProductCategory, ProductSubCategory, ProductVendor

class ProductCategorySerializer(serializers.ModelSerializer):
    categoryName = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = ('categoryName', 'slug')

    def get_categoryName(self, obj):
        return obj.category.name
    
    def get_slug(self, obj):
        return obj.category.slug

class ProductSubCategorySerializer(serializers.ModelSerializer):
    subCategoryName = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()

    class Meta:
        model = ProductSubCategory
        fields = ('subCategoryName', 'slug')

    def get_subCategoryName(self, obj):
        return obj.subCategory.name

    def get_slug(self, obj):
        return obj.subCategory.slug


class ProductVendorSerializer(serializers.ModelSerializer):
    VendorName = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()

    class Meta:
        model = ProductVendor
        fields = ('VendorName', 'slug')

    def get_VendorName(self, obj):
        return obj.Vendor.name

    def get_slug(self, obj):
        return obj.Vendor.slug
