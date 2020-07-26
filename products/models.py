from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    features = models.TextField()
    specifications_sensor = models.CharField(max_length=254, default='')       
    specifications_sensor_resolution = models.CharField(max_length=254, default='')
    specifications_sensor_peak = models.CharField(max_length=254, default='')
    specifications_sensor_read_noise = models.CharField(max_length=254, default='')
    specifications_sensor_pixel = models.CharField(max_length=254, default='')
    specifications_sensor_size = models.CharField(max_length=254, default='')
    specifications_environmental_storage_temperature = models.CharField(max_length=254, default='')
    specifications_environmental_operating_temperature = models.CharField(max_length=254, default='')
    specifications_environmental_storage_humidity = models.CharField(max_length=254, default='')
    specifications_environmental_operating_humidity = models.CharField(max_length=254, default='')
    specifications_mechanical_diameter = models.CharField(max_length=254, default='')
    specifications_mechanical_length = models.CharField(max_length=254, default='')
    specifications_mechanical_weight = models.CharField(max_length=254, default='')
    specifications_powerconnectivity_usb = models.CharField(max_length=254, default='')
    specifications_powerconnectivity_telescope = models.CharField(max_length=254, default='')
    specifications_powerconnectivity_input = models.CharField(max_length=254, default='')
    specifications_powerconnectivity_supply = models.CharField(max_length=254, default='')
    specifications_powerconnectivity_consumption = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    featured = models.BooleanField()

    def __str__(self):
        return self.name
        
