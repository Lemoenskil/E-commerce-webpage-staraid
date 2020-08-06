from .views import index, payment_and_shipping
from django.urls import path, re_path


urlpatterns = [
    re_path(r'payment_and_shipping/', payment_and_shipping, name='payment_and_shipping'),
    re_path(r'', index, name="index"),
    
]