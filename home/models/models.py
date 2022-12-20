from django.db.models import TextField, DecimalField, CharField, JSONField, Model, ImageField, ForeignKey, CASCADE, \
    SET_NULL
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.django.base import BaseModel, SlugBaseModel


# Create your models here.
class Category(BaseModel, SlugBaseModel, MPTTModel):
    parent = TreeForeignKey('self', SET_NULL, 'children', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += str(Category.objects.filter(slug=self.slug).count())
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class MPTTMeta:
        order_insertion_by = ['name']



class Shops(BaseModel, SlugBaseModel):
    photo = ImageField(upload_to='media/shops/%y/%m/%d')
    inform = TextField(max_length=5000)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += str(Category.objects.filter(slug=self.slug).count())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(BaseModel, SlugBaseModel):
    description = JSONField(max_length=3000)
    category = ForeignKey(Category, on_delete=CASCADE)
    price = DecimalField(max_digits=50, decimal_places=10)
    brand = CharField(max_length=150)
    shop = ForeignKey(Shops, on_delete=CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += str(Category.objects.filter(slug=self.slug).count())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(Model):
    product = ForeignKey(Product, CASCADE)
    photo = ImageField(upload_to='media/product/y/m/d')
