from .views import index, payment_and_shipping, returns_and_warranty
from django.urls import path, re_path


urlpatterns = [
    re_path(r'payment_and_shipping/', payment_and_shipping, name='payment_and_shipping'),
    re_path(r'returns_and_warranty/', returns_and_warranty, name='returns_and_warranty'),
    re_path(r'', index, name="index"),
    
]