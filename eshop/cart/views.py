from django.shortcuts import render
from .models import Cart
from .serializer import CartSerializer, CartSerializerWithProduct
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework import authentication, generics
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class add_to_cart(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [authentication.TokenAuthentication,  authentication.SessionAuthentication]
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            in_cart = Cart.objects.filter(user=self.request.user, product=serializer.validated_data['product'])
            if in_cart:
                in_cart.update(quantity=in_cart[0].quantity+serializer.validated_data['quantity'], price=serializer.validated_data['price'])
                # return the updated cart
                serializer = CartSerializerWithProduct(in_cart[0])
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                serializer.save(user=self.request.user, price=serializer.validated_data['product'].price)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class get_cart(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializerWithProduct
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    authentication_classes = [authentication.TokenAuthentication,  authentication.SessionAuthentication]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cart.objects.filter(user=self.request.user)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class get_cart_by_id(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializerWithProduct
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    authentication_classes = [authentication.TokenAuthentication,  authentication.SessionAuthentication]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cart.objects.filter(user=self.request.user)
        else:
            return Cart.objects.none()

class delete_cart_data(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    authentication_classes = [authentication.TokenAuthentication,  authentication.SessionAuthentication]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cart.objects.filter(id=self.kwargs['id'], user=self.request.user)
        else:
            return Cart.objects.none()