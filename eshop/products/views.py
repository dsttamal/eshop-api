from django.shortcuts import render
from .models import  Product
from .serializer import ProductSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

# Create your views here.
# get all products from database with pagination and filter
class get_products(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class get_product_by_category_subCategory_Vendor(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    def get_queryset(self):
        slug = self.kwargs['slug']
        if(self.kwargs['type'] == 'category'):
            return Product.objects.filter(productcategory__category__slug=slug)
        elif(self.kwargs['type'] == 'subcategory'):
            return Product.objects.filter(productsubcategory__subCategory__slug=slug)
        elif(self.kwargs['type'] == 'Vendor'):
            return Product.objects.filter(productVendor__Vendor__slug=slug)
        else:
            return Product.objects.none()

class get_product_by_id(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'