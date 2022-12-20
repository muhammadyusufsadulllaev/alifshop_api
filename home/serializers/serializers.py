from rest_framework.serializers import ModelSerializer

from home.models.models import Category, Shops, Product, ProductImage


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class ShopsModelSerializer(ModelSerializer):
    class Meta:
        model = Shops
        exclude = ('slug',)


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ('slug',)


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ()
