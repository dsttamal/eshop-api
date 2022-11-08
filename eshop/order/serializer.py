from .models import orderProduct
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderProduct
        fields = ('id', 'product', 'quantity', 'price', 'total', 'address', 'city', 'state', 'zip', 'order_date', 'is_active', 'is_delivered')

