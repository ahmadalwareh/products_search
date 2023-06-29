from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer


class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Product.objects.all()

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price and max_price:
            queryset = queryset.filter(price__range=(min_price, max_price))

        return queryset
