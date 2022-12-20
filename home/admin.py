from django.contrib import admin
from django.contrib.admin import ModelAdmin

from home.models.models import Category, Shops, Product, ProductImage


# Register your models here.
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Shops)
class ShopsAdmin(ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(ModelAdmin):
    pass
