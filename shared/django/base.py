from django.db.models import Model, CharField, DateTimeField, SlugField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugBaseModel(Model):
    name = CharField(max_length=150)
    slug = SlugField(max_length=150, unique=True,blank=True)

    class Meta:
        abstract = True
