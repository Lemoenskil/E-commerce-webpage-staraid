from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    features = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    featured = models.BooleanField()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
        
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    name = models.ImageField(upload_to='uploads')
    order = models.IntegerField(blank = True, null = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('order',)

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, related_name='specifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    value = models.CharField(max_length=254)
    order = models.IntegerField(blank = True, null = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('order',)
