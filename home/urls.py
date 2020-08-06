from .views import index, payment_and_shipping, returns_and_warranty, terms_and_conditions, privacy, cookies
from django.urls import path, re_path


urlpatterns = [
    re_path(r'payment_and_shipping/', payment_and_shipping, name='payment_and_shipping'),
    re_path(r'returns_and_warranty/', returns_and_warranty, name='returns_and_warranty'),
    re_path(r'terms_and_conditions/', terms_and_conditions, name='terms_and_conditions'),
    re_path(r'cookies/', cookies, name='cookies'),
    re_path(r'privacy/', privacy, name='privacy'),
    re_path(r'', index, name="index"),
    
]
