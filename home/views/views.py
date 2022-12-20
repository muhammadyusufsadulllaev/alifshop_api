from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from home.models.models import Category, Shops, Product, ProductImage
from home.serializers.serializers import CategoryModelSerializer, ShopsModelSerializer, ProductModelSerializer, \
    ProductImageModelSerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shops.objects.all()
    serializer_class = ShopsModelSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {'price': ['gte', 'lte'], 'category': ['exact'], 'brand': ['exact']}


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageModelSerializer
