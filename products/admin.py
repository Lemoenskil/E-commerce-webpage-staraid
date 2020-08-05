from django.contrib import admin
from django import forms
from django.conf import settings
from .models import Product, ProductImage, ProductSpecification

# Register your models here.
class ProductForm(forms.ModelForm):
    model = Product
    class Media:
        js = (
            settings.STATIC_URL + 'js/jquery-3.2.1.min.js',
            settings.STATIC_URL + 'js/jquery-ui-1.12.1.min.js',
            settings.STATIC_URL + 'js/item-sort.js',
        )

class ProductSpecificationInline(admin.StackedInline):
    model = ProductSpecification
    extra = 0

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ProductSpecificationInline ]
    form = ProductForm

admin.site.register(Product, ProductAdmin)

