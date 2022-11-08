from django.shortcuts import render
from .models import  orderProduct
from .serializer import OrderSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework import authentication, generics
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class get_orders(generics.ListAPIView):
    queryset = orderProduct.objects.all()
    serializer_class = OrderSerializer
    search_fields = ['user']
    authentication_classes = [authentication.TokenAuthentication,  authentication.SessionAuthentication]

class get_order_by_id(generics.RetrieveAPIView):
    queryset = orderProduct.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    authentication_classes = [authentication.TokenAuthentication,  authentication.SessionAuthentication]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return orderProduct.objects.filter(user=self.request.user)
        else:
            return orderProduct.objects.none()    

class get_order_by_user(generics.ListAPIView):
    queryset = orderProduct.objects.all()
    serializer_class = OrderSerializer
    search_fields = ['user']
    authentication_classes = [authentication.TokenAuthentication,  authentication.SessionAuthentication]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return orderProduct.objects.filter(user=self.request.user)
        else:
            return orderProduct.objects.none()

class add_order(generics.CreateAPIView):
    queryset = orderProduct.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [authentication.TokenAuthentication,  authentication.SessionAuthentication]
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user, is_active=True, is_delivered=False, updated_at=None, price=serializer.validated_data['product'].price)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
