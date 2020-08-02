from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Defines the user profile. A user profile captures profile information
    associated with a user account.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birthdate = models.DateField(verbose_name="birthdate")
    full_name = models.CharField(verbose_name="fullname", max_length=50, blank=False)
    phone_number = models.CharField(verbose_name="phone number", max_length=20, blank=False)
    country = models.CharField(verbose_name="country", max_length=40, blank=False)
    postcode = models.CharField(verbose_name="postcode", max_length=20, blank=False)
    town_or_city = models.CharField(verbose_name="town or city", max_length=40, blank=False)
    street_address1 = models.CharField(verbose_name="street address 1", max_length=40, blank=False)
    street_address2 = models.CharField(verbose_name="street address 2", max_length=40, blank=True)
