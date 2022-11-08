from .models import ProductCategory, ProductSubCategory, ProductVendor
from .serializer import ProductCategorySerializer, ProductSubCategorySerializer, ProductVendorSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django.db.models import CharField, Value
# Create your views here.
class get_category(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']
    # def get_queryset(self):
    #     return ProductCategory.objects.annotate(url_to_get_products=Value('product/category/'+('category__slug')+'/', output_field=CharField()))

class get_sub_category(generics.ListAPIView):
    queryset = ProductSubCategory.objects.all()
    serializer_class = ProductSubCategorySerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['subCategory__name']

class get_vendor(generics.ListAPIView):
    queryset = ProductVendor.objects.all()
    serializer_class = ProductVendorSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['Vendor__name']